import ezsheets
 ezsheets.convertAddress('A2') # Converts addresses...
(1, 2)
ezsheets.convertAddress(1, 2) # ...and converts them back, too.
'A2'
ezsheets.getColumnLetterOf(2)
ezsheets.getColumnNumberOf('B')
2
 ezsheets.getColumnLetterOf(999)
'ALK'
ezsheets.getColumnNumberOf('ZZZ')
18278
