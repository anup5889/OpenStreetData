import xlrd

book= xlrd.open_workbook("2013_ERCOT_Hourly_Load_Data.xls")

print "The number of worksheets is", book.nsheets
print "Worksheet name(s):", book.sheet_names()
sheet = book.sheet_by_index(0)
print sheet.name, sheet.nrows, sheet.ncols
print "Cell D30 is", sheet.cell_value(rowx=29, colx=3)
data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
#print data
cv=sheet.col_values(1,start_rowx=1,end_rowx=None) # taking the first column of sheet


maxvalue=max(cv)
minvalue=min(cv)

maxpos=cv.index(maxvalue)+1
maxtime=sheet.cell_value(maxpos,0)
realtime=xlrd.xldate_as_tuple(maxtime,0)

print maxvalue, realtime
print minvalue





        
