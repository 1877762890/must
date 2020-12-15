from day16.bank1.Savetils import MysqlUtils
from  day16.bank1.SaveMoney import SaveMoney
import os
class DataRead:
    list=None #全局列表 mode=excel,filename  sheetname
    # database:database,user,password,tablename
    def __init__(self,mode,filename="",sheetname="0",host="localhost",database="",user="",password="",tablename=""):
        if mode == "excel":
            if filename == "":
                raise Exception("文件名不能为空！别瞎弄！")
            elif not os.path.isfile(filename):
                raise Exception("文件名不存在！别瞎弄！")
            else:
                DataRead.list = SaveMoney.read(filename,sheetname)
        elif mode == "database":
            DataRead.list = MysqlUtils.read(host=host,database=database,user=user,password=password,tablename=tablename)
        else:
            raise  Exception("对不起，您的操作模式无法识别！")
# d=DataRead("database",database="bank",tablename="testdata",user="root",password="")
# d=DataRead("excel",filename="D:\\pythonProject1\\day16\\bank1\\c.xlsx",sheetname="0")
# print(d.list)