def leer_excel():
    import xlrd 

    filePath = "C:\\Users\\ruben\\Documents\\Python\\excel_ejemplo.xls"

    openFile = xlrd.open_workbook(filePath)

    sheet = openFile.sheet_by_name("Hoja1")
    
    for i in range (sheet.nrows):
        print(sheet.cell_value(i,0), "   ",sheet.cell_value(i,1))