import  unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from day16.bank1.DataRead3 import DataRead
from day16.bank1.bankdemo2 import bank_saveMoney
#数据源
# data1=DataRead("database",database="bank",tablename="testdata",user="root",password="root").list
data1=DataRead("excel",filename="D:\\pythonProject1\\day16\\bank1\\c.xlsx",sheetname="0").list
@ddt

class TestCalc(unittest.TestCase):

    @data(*data1)
    @unpack
    def testSaveMoney(self,a,m,c):
        s=bank_saveMoney(ac=a,money=m)
        self.assertEqual(s,c)











