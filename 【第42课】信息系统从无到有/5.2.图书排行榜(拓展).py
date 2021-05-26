import win32com.client


mdb_file = "Database.accdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
# 查询语句

sql = """SELECT
             TOP 8
             [ISBN],
                 (SELECT [书名] FROM [book] WHERE [ISBN]=[borrow].[ISBN]) AS [书名],
                 COUNT(*) AS [借阅数量]
             FROM [borrow]
             GROUP BY [ISBN]
             ORDER BY COUNT(*) DESC
         """  # 聚合字段别名不能用于排序
rs.Open(sql, conn, 1, 1)

print('查询到{}条记录：\n'.format(rs.RecordCount))
# 遍历记录，读取数据
rs.MoveFirst()  # 光标移到首条记录
while not rs.EOF:
    for i in range(rs.Fields.Count):
        print('  {}: {}'.format(rs.Fields[i].Name, rs.Fields[i].Value))    # 字段名：字段内容
    print(end='\n')
    rs.MoveNext()  # 光标移到下条记录

conn.Close()
