import xlrd
class SaveMoney:
    @classmethod
    def read(cls,filename="",sheetname="0"):
        try:
            list=[]
            # 打开文件
            file = xlrd.open_workbook(filename,)
            if sheetname.isdigit(): #如果您的选项卡是数字
                # 获取选项卡

                sheet=file.sheet_by_index(int(sheetname))
                # 获取所有行
                rows=sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
                return list
            else:
                sheet=file.sheet_by_name(sheetname)
                rows=sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
                return list
        except Exception as error:
            print(error)
# result=SaveMoney.read("D:\\pythonProject1\\day16\\bank1\\c.xlsx","Sheet1")
# print(result)



