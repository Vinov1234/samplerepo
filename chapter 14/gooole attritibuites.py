import ezsheets
ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
ss.title         # The title of the spreadsheet.
'Education Data'
ss.title = 'Class Data' # Change the title.
ss.spreadsheetId # The unique ID (this is a read-only attribute).
'1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU'
ss.url           # The original URL (this is a read-only attribute).
'https://docs.google.com/spreadsheets/d/1J-Jx6Ne2K_vqI9J2SO-
TAXOFbxx_9tUjwnkPC22LjeU/'
ss.sheetTitles     # The titles of all the Sheet objects
('Students', 'Classes', 'Resources')
ss.sheets          # The Sheet objects in this Spreadsheet, in order.
(<Sheet sheetId=0, title='Students', rowCount=1000, columnCount=26>, <Sheet
sheetId=1669384683, title='Classes', rowCount=1000, columnCount=26>, <Sheet
sheetId=151537240, title='Resources', rowCount=1000, columnCount=26>)
ss[0]              # The first Sheet object in this Spreadsheet.
ss['Students']     # Sheets can also be accessed by titl
 del ss[0]          # Delete the first Sheet object in this Spreadsheet.
ss.sheetTitles     # The "Students" Sheet object has been deleted:
('Classes', 'Resources')
