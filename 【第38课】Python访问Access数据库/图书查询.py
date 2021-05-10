import win32com.client


conn = win32com.client.Dispatch(r"ADODB.Connection")
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = 图书借阅管理.mdb'  # Access2007及以后
conn.Open(DSN)
# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
# 查询语句
sql = "SELECT * FROM books WHERE 数量<5 OR 类型='教材'"
rs.Open(sql, conn, 1, 1)

print('查询到{}条记录：\n'.format(rs.RecordCount))
# 遍历记录，读取数据
rs.MoveFirst()  #光标移到首条记录
while not rs.EOF:
    for i in range(rs.Fields.Count):
        print('  {}: {}'.format(rs.Fields[i].Name, rs.Fields[i].Value))    # 字段名：字段内容
    print(end='\n')
    rs.MoveNext()  # 光标移到下条记录

conn.Close()
