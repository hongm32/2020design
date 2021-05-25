import win32com.client

mdb_file = "../【第37课】数据库的构建/图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

rs = win32com.client.Dispatch(r'ADODB.Recordset')
table = 'books'
sql = """SELECT * FROM {}""".format(table)
rs.Open(sql, conn, 1, 3)

print('表{}已有{}条记录'.format(table, rs.RecordCount))
print("新增记录：")

rs.AddNew()  # 添加记录到数据表末端
for i in range(rs.Fields.Count):
    while True:
        temp = input('  {}: '.format(rs.Fields[i].Name))
        if temp:
            if rs.Fields[i].Type == 3:
                rs.Fields[i].Value = int(temp)
            else:
                rs.Fields[i].Value = temp
            break

rs.Update()  # 更新数据表记录

conn.Close()  # 关闭连接
