import win32com.client


mdb_file = "../【第37课】数据库的构建/图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

rs = win32com.client.Dispatch(r'ADODB.Recordset')
table = 'books'
sql = """SELECT * FROM books"""
rs.Open(sql, conn, 1, 3)

print('表{}已有{}条记录'.format(table, rs.RecordCount))
info = []
fields_name = []
for i in range(rs.Fields.Count):
    fields_name.append(rs.Fields[i].Name)
    while True:
        temp = input('{}: '.format(rs.Fields[i].Name))
        if temp:
            if rs.Fields[i].Type == 3:
                info.append(int(temp))
            else:
                info.append(temp)
            break

sql = "INSERT INTO {}{} VALUES {}".format(table, str(tuple(fields_name)).replace("'", ""), tuple(info))
conn.Execute(sql)  # 执行sql语句

conn.Close()
