import win32com.client

mdb_file = "../【第37课】数据库的构建/图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

rs = win32com.client.Dispatch(r'ADODB.Recordset')
table = 'book'
sql = """SELECT * FROM {}""".format(table)
rs.Open(sql, conn, 1, 3)

print('表{}已有{}条记录'.format(table, rs.RecordCount))

rs.AddNew()  # 添加记录到数据表末端
# 更新各字段的值
rs("ISBN").Value = '978-7-5499-8387-2'
rs("书名").Value = "教育写作"
rs("作者").Value = '颜莹'
rs("类型").Value = '教育'
rs("出版日期").Value = '202-3-1'
rs("数量").Value = 9

rs.Update()  # 更新数据表记录

conn.Close()  # 关闭连接
