import win32com.client


mdb_file = "../【第37课】数据库的构建/图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
sql = """SELECT * FROM [book]"""
rs.Open(sql, conn, 1, 3)

# 光标移到首条记录
rs.MoveFirst()

# 遍历记录，读取数据
while not rs.EOF:
    for i in range(rs.Fields.Count):
        print('{}: {}'.format(rs.Fields[i].Name, rs.Fields[i].Value))    # 字段名：字段内容
    print(end='\n')
    rs.MoveNext()  # 光标移到下条记录

print('该表有{}个字段'.format(rs.Fields.Count))
print('该表有{}条记录'.format(rs.RecordCount))

# 关闭连接
conn.Close()
