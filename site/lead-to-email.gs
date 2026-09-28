/**
 * Built for Main Street: website leads to your inbox and a Google Sheet.
 * Runs inside your own Google account. No outside service, nothing to pay for.
 *
 * SET UP ONCE (about five minutes)
 * 1. Signed in as the Google account you want sending the emails, go to
 *    sheets.new and name the sheet "Built for Main Street leads".
 * 2. In that sheet: Extensions > Apps Script. Delete what's there, paste this
 *    whole file, and click Save.
 * 3. Deploy > New deployment > gear icon > Web app.
 *    Execute as: Me.   Who has access: Anyone.   Click Deploy.
 * 4. Google asks for permission to send email and edit this sheet. Allow it.
 *    (If it says the app isn't verified: Advanced > Go to project. It's yours.)
 * 5. Copy the Web app URL. In site/www/index.html, replace
 *    https://script.google.com/macros/s/PASTE_YOUR_SCRIPT_ID/exec with it.
 *
 * Each lead is emailed to TO below and added as a row to the sheet. The
 * subject reads "Free check: <shop> (<town>)", and replying goes straight
 * to the customer when they left an email.
 *
 * If you change this code later: Deploy > Manage deployments > edit >
 * Version: New version. The URL stays the same.
 */
const TO = 'hello@builtformainstreet.com';

function doPost(e) {
  const p = (e && e.parameter) || {};
  if (p['company-url']) return done_();          // a bot filled the hidden field

  const lock = LockService.getScriptLock();
  lock.tryLock(10000);
  try {
    const when = new Date();
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Received', 'Name', 'Shop', 'Town', 'Phone', 'Email']);
      sheet.setFrozenRows(1);
    }
    sheet.appendRow([when, p.name || '', p.business || '', p.town || '', p.phone || '', p.email || '']);

    const subject = p.subject || ('Free check: ' + (p.business || 'new request'));
    const body = [
      'New free check request from the website.',
      '',
      'Name:   ' + (p.name || ''),
      'Shop:   ' + (p.business || ''),
      'Town:   ' + (p.town || ''),
      'Phone:  ' + (p.phone || ''),
      'Email:  ' + (p.email || 'not given'),
      '',
      'Received ' + when.toString(),
    ].join('\n');
    const opts = { name: 'Built for Main Street website' };
    if (p.email) opts.replyTo = p.email;
    MailApp.sendEmail(TO, subject, body, opts);
  } finally {
    lock.releaseLock();
  }
  return done_();
}

// Opening the URL in a browser shows this, which confirms the deployment is live.
function doGet() {
  return ContentService.createTextOutput('Built for Main Street lead form is running.');
}

function done_() {
  return ContentService.createTextOutput('ok');
}
