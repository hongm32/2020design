import win32com.client
import time


mdb_file = "Database.accdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接


# 学生登陆[student]

sql = """SELECT
             """
rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs.Open(sql, conn, 1, 1)
if rs.EOF:
    pass
else:
    pass


# 查询能借(库存数量大于0)的图书[book]
sql = """SELECT
             """
rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs.Open(sql, conn, 1, 1)
if rs.EOF:
    pass
else:
    pass


# 添加借书记录[borrow]
today = time.strftime('%Y-%m-%d ', time.localtime(time.time()))  # 获取当前日期，作为借阅日期
sql = """INSERT
             """
conn.Execute(sql)


# 更新库存数量[book]
sql = """UPDATE
             """
conn.Execute(sql)
