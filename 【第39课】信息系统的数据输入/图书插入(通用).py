import win32com.client

tablename = "books"
conn = win32com.client.Dispatch(r"ADODB.Connection")
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = 图书借阅管理.mdb'  # Access2007及以后
conn.Open(DSN)
rs = win32com.client.Dispatch(r'ADODB.Recordset')
# sql = 'books'
sql = "SELECT * FROM books"
rs.Open(sql, conn, 1, 3)

print('表{}已有{}条记录'.format(tablename, rs.RecordCount))
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

sql = "INSERT INTO {}{} VALUES {}".format(tablename, str(tuple(fields_name)).replace("'", ""), tuple(info))
conn.Execute(sql)  # 执行sql语句

conn.Close()
