import openpyxl
wb = openpyxl.load_workbook(filename = "C:\\Users\\pc\\Documents\\Automated the boring stuff\\chapter 13\\examplenum.xlsx")
sheet = wb['Sheet1']
tuple(sheet['A1':'C3']) 
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
      print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')
