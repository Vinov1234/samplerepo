import ezsheets
ss = ezsheets.createSpreadsheet('Delete me') # Create the spreadsheet.
ezsheets.listSpreadsheets() # Confirm that we've created a spreadsheet.
{'1aCw2NNJSZblDbhygVv77kPsL3djmgV5zJZllSOZ_mRk': 'Delete me'}
ss.delete() # Delete the spreadsheet.
ezsheets.listSpreadsheets()
{}
