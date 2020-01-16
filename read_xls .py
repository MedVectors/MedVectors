import xlrd

file_name = "C:/Users/admin/Downloads/Telegram Desktop/perinatal.xlsx"

wb = xlrd.open_workbook(file_name)
sheet = wb.sheet_by_index(0)

print("Строк всего " + sheet.nrows.__str__())
print("Столбцов всего " + sheet.ncols.__str__())

print("НАЗВАНИЯ СТОЛБЦОВ")
for i in range(sheet.ncols):
    print(i, sheet.cell_value(0, i))

print("СОДЕРЖИМОЕ СТОЛБЦА 23")
dead = []
for i in range(sheet.nrows):
    if sheet.cell_value(i, 23) != "":
        print(i, sheet.cell_value(i, 23))
        dead.append(i)

print("All dead indexes")
print(dead)

print("Содержимое строки 1")
print(sheet.row_values(0))

print("строки где смерть")
for i in dead:
    print(sheet.row_values(i))