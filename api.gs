/**
 * 1. Set sheetId and column name
 * 2. Add Google Sheets API to the Apps Script project
 * 3. Deploy project as web app (Execute as `Me', Who has access `Anyone')
 */

const sheetId = 'my sheet id'; // Obtain from the Google Sheets URL
const columnName = 'E';

/**
 * Retuns the number of rows in a sheet (minus `numberOfHeaderRows`)
 * or {} if an error occured
 */
function countCommitteeSignups(sheetId, numberOfHeaderRows = 1) {
  const range = `${columnName}${1 + numberOfHeaderRows}:${columnName}999`;
  let signupCounts = {};
  try {
    const values = Sheets.Spreadsheets.Values.get(sheetId, range).values;
    values.forEach(value => {
      value[0].split(',').forEach(committe => {
        committe = committe.trim();
        if (signupCounts[committe] == null) {
          signupCounts[committe] = 1;
        }
        else {
          signupCounts[committe] += 1;
        }
      });
    });
  } catch (e) {
    console.error(`Invocation countRowsInSpreadsheet(sheetId = ${sheetId}, numberOfHeaderRows = ${numberOfHeaderRows}) encountered ${e}`);
  }
  return signupCounts;
}

/**
 * API following JSend specification (https://github.com/omniti-labs/jsend)
 */
function doGet() {
  let data = countCommitteeSignups(sheetId);
  const jsendResponse = {
    'status': 'success',
    'data': data,
  };
  const jsendOutput = JSON.stringify(jsendResponse);
  console.log(jsendOutput);
  return ContentService.createTextOutput(jsendOutput).setMimeType(ContentService.MimeType.JSON);
}
