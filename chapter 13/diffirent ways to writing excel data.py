from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
sheet["A1"] = 100
sheet ["A2"] = 10.123
sheet ["A3"] = "welcome"
import time
now = time.strftime("%x")
sheet["A4"] = now
wb.save(filename = "C:\\Users\\pc\\Documents\\Automated the boring stuff\\chapter 13\\part3.xlsx")
v1 = sheet["b1"]
v1.value = 200
sheet.cell(row=3,column=3).value = 2000
wb.save ("C:\\Users\\pc\\Documents\\Automated the boring stuff\\chapter 13\\part3.xlsx")
