/**
 * Built for Main Street: the call sheet keeps this Google Sheet up to date.
 * One clean row per lead, updated in place every time you tap a status or edit a lead.
 * You never have to type in it. It's there when you want to look, sort or share.
 *
 * Setup, about 5 minutes:
 *  1. Open the Sheet "Built for Main Street · Call List" (in hello@'s Drive).
 *  2. Extensions > Apps Script. Delete what's there, paste this whole file.
 *  3. Change KEY below to any word only you know. Save.
 *  4. Deploy > New deployment > Select type: Web app.
 *     Execute as: Me.  Who has access: Anyone.  Deploy, and allow access.
 *  5. Copy the Web app URL (ends in /exec).
 *  6. Call sheet > Script > Your details: paste the URL into "Google Sheet sync URL"
 *     and the word into "Sheet key". Then tap "Send every lead to the Sheet now".
 *     The first send clears the old starter rows and lays the Sheet out cleanly.
 *
 * "Anyone" means anyone with the URL could send rows, which is why the key word
 * is checked. Keep the URL private.
 */
const KEY = 'change-this-word';
const HEAD = ['Business','Phone','Where','Kind','Status','Calls','Last call','Next step','Plan','Preview','Problem','Email','Notes','id'];
const WIDTH = [220, 125, 150, 100, 105, 55, 125, 90, 160, 70, 120, 200, 420, 60];
const COLORS = {
  'talked': '#d9ead3', 'check booked': '#b6d7a8', 'offer made': '#a4c2f4', 'sold': '#6aa84f',
  'no answer': '#fff2cc', 'voicemail': '#fff2cc', 'emailed': '#fff2cc', 'hung up': '#f4cccc', 'dead': '#d9d9d9'
};

function layout_(sh) {
  sh.clear();
  sh.getRange(1, 1, 1, HEAD.length).setValues([HEAD]).setFontWeight('bold').setBackground('#16191a').setFontColor('#ffffff');
  sh.setFrozenRows(1);
  WIDTH.forEach((w, i) => sh.setColumnWidth(i + 1, w));
  sh.getRange('B:B').setNumberFormat('@');
  sh.getRange('M:M').setWrap(true);
  sh.hideColumns(HEAD.length);  // the id column only matches rows; you never need it
  const statusCol = sh.getRange(2, 5, 1000, 1);
  sh.setConditionalFormatRules(Object.keys(COLORS).map(k =>
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo(k).setBackground(COLORS[k])
      .setRanges([statusCol]).build()));
}

function upsert_(sh, r) {
  const last = sh.getLastRow();
  const idCol = HEAD.length;
  const ids = last > 1 ? sh.getRange(2, idCol, last - 1, 1).getValues().map(x => String(x[0])) : [];
  const row = HEAD.map(k => (r[k] == null ? '' : String(r[k]).slice(0, 2000)));
  const i = ids.indexOf(String(r.id));
  if (i >= 0) sh.getRange(i + 2, 1, 1, HEAD.length).setValues([row]);
  else sh.appendRow(row);
}

function handle_(body) {
  if (!body || body.k !== KEY) return 'bad key';
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const sh = SpreadsheetApp.getActive().getSheets()[0];
    const first = sh.getLastRow() ? sh.getRange(1, 1, 1, HEAD.length).getValues()[0].join('|') : '';
    if (first !== HEAD.join('|')) layout_(sh);
    (body.rows || []).forEach(r => upsert_(sh, r));
    return 'ok';
  } finally {
    lock.releaseLock();
  }
}

function doPost(e) {
  return ContentService.createTextOutput(handle_(JSON.parse(e.postData.contents)));
}

function doGet(e) {
  const out = e.parameter.d ? handle_(JSON.parse(e.parameter.d)) : 'ready';
  return ContentService.createTextOutput(out);
}
