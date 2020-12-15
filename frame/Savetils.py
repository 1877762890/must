import pymysql

class MysqlUtils:
    con=None # 全局连接
    cursor=None # 全局游标

    @classmethod #类方法
    def read(cls,host="localhost",database="银行数据库",user="root",password="",tablename="saveMoney"):
        # 获取连接
        cls.con=pymysql.connect(host=host,user=user,password=password,database=database,charset="utf8")
        # 获取游标
        cls.cursor=cls.con.cursor()
        # 返回参数化数据
        sql='''
           select * from {tablename}
        '''
        cls.cursor.execute(sql.format(tablename=tablename))
        return cls.cursor.fetchall()

# k=MysqlUtils.read()
# print(k)