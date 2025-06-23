from openpyxl import Workbook

w = Workbook()
wd = w.active

wd.title = "Sheet1"
wd['A1'] = "Name"
wd['B1'] = "Age"
wd.append(["Maha", 21])
wd.append(["janani", 25])

w.save(r"E:\HEXAWARE\PYTHON PROGRAMS\excelsample.xlsx")
