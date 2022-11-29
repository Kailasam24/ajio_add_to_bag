from Library.config import Config
import xlrd
list_1=[('9966250321','kurthi')]
class ReadExcel():
    def read_testdata(self,sheetname):
        wb=xlrd.open_workbook(Config.Data_path)
        ws=wb.sheet_by_name(sheetname)
        columns=ws.ncols
        rows=ws.get_rows()
        header=next(rows)
        data=[]
        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            # data.append(int(values[0]))
            data.append(values)
        return data


    def read_locators(self,sheetname):
        wb = xlrd.open_workbook(Config.Locator_Path)
        ws= wb.sheet_by_name(sheetname)
        rows=ws.get_rows()
        header=next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d

    #print(read_locators())