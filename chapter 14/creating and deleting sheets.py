import ezsheets
ss = ezsheets.createSpreadsheet('Multiple Sheets')
ss.sheetTitles
('Sheet1',)
ss.createSheet('Spam') # Create a new sheet at the end of the list of
sheets.

ss.createSheet('Eggs') # Create another new sheet.
ss.sheetTitles
('Sheet1', 'Spam', 'Eggs')
ss.createSheet('Bacon', 0) code># Create a sheet at index 0 in the list of
sheets
ss.sheetTitles
('Bacon', 'Sheet1', 'Spam', 'Eggs')
