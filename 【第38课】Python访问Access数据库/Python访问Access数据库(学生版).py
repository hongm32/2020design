import win32com.client


mdb_file = "图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
try:
    DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007以前版本
    conn.Open(DSN)  # 用游标打开数据连接
except:
    DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后版本
    conn.Open(DSN)  # 用游标打开数据连接

# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
sql = """SELECT * FROM books"""
rs.Open(sql, conn, 1, 1)

rs.MoveFirst()  # 光标移到首条记录
print("{}:{}".format(rs.Fields[0].Name, rs.Fields[0].Value))




# 关闭连接
conn.Close()
