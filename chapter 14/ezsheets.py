ss.sheetTitles
('Bacon', 'Sheet1', 'Spam', 'Eggs')
ss[0].delete()      # Delete the sheet at index 0: the "Bacon" sheet.
ss.sheetTitles
('Sheet1', 'Spam', 'Eggs')
ss['Spam'].delete() # Delete the "Spam" sheet.
ss.sheetTitles
('Sheet1', 'Eggs')
sheet = ss['Eggs']  # Assign a variable to the "Eggs" sheet.
sheet.delete()      # Delete the "Eggs" sheet.
ss.sheetTitles
('Sheet1',)
ss[0].clear()       # Clear all the cells on the "Sheet1" sheet.
ss.sheetTitles      # The "Sheet1" sheet is empty but still exists.
('Sheet1',)
