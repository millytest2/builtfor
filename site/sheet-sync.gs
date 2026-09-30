/**
 * Built for Main Street: the call sheet writes every lead into this Google Sheet.
 * One row per lead, updated in place each time you tap a status or edit a lead.
 *
 * Setup, about 5 minutes:
 *  1. Create a new Google Sheet (signed in as hello@ or your own account).
 *  2. Extensions > Apps Script. Delete what's there, paste this whole file.
 *  3. Change KEY below to any word only you know. Save.
 *  4. Deploy > New deployment > Select type: Web app.
 *     Execute as: Me.  Who has access: Anyone.  Deploy, and allow access.
 *  5. Copy the Web app URL (ends in /exec).
 *  6. Call sheet > Script > Your details: paste the URL into "Google Sheet sync URL"
 *     and the word into "Sheet key". Then tap "Send every lead to the Sheet now".
 *
 * "Anyone" means anyone with the URL could send rows, which is why the key word
 * is checked. Keep the URL private.
 */
const KEY = 'change-this-word';
const HEAD = ['id','business','phone','city','state','status','touches','last_touch','next','plan','email','website','notes','updated'];

function upsert_(sh, r) {
  const last = sh.getLastRow();
  const ids = last > 1 ? sh.getRange(2, 1, last - 1, 1).getValues().map(x => String(x[0])) : [];
  const row = HEAD.map(k => (r[k] == null ? '' : String(r[k]).slice(0, 5000)));
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
    if (sh.getLastRow() === 0) { sh.appendRow(HEAD); sh.setFrozenRows(1); }
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
