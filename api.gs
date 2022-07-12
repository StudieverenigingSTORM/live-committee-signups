/**
 * 1. Set up sheets below
 * 2. Add Google Sheets API to the Apps Script project
 * 3. Deploy project as web app (Execute as `Me', Who has access `Anyone')
 */


/**
 * Mapping of names to Google Sheet IDs (obtain from URL)
 */
const sheets = {
  /* 'myTable' : '<Google Sheet ID>', */
};

/**
 * Retuns the number of rows in a sheet (minus `numberOfHeaderRows`)
 * or -1 if an error occured
 */
function countRowsInSpreadsheet(sheetId, numberOfHeaderRows = 1) {
  const range = 'A1:A999';
  try {
    const values = Sheets.Spreadsheets.Values.get(sheetId, range).values;
    return values.length - numberOfHeaderRows;
  } catch(e) {
    console.error(`Invocation countRowsInSpreadsheet(sheetId = ${sheetId}, numberOfHeaderRows = ${numberOfHeaderRows}) encountered ${e}`);
    return -1;
  }
}

/**
 * API following JSend specification (https://github.com/omniti-labs/jsend)
 */
function doGet() {
  let data = Object.assign({}, sheets);
  Object.keys(sheets).map(key => data[key] = countRowsInSpreadsheet(sheets[key]));
  const jsendResponse = {
    'status': 'success',
    'data': data,
  };
  const jsendOutput = JSON.stringify(jsendResponse);
  console.log(jsendOutput);
  return ContentService.createTextOutput(jsendOutput).setMimeType(ContentService.MimeType.JSON);
}
