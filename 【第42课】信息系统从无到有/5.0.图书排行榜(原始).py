import win32com.client


mdb_file = "Database.accdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
# 查询语句
sql = """SELECT 
             [ISBN]
             FROM [book]
"""
rs.Open(sql, conn, 1, 1)
books_isbn = rs.GetRows()[0]

book_count = []
for isbn in books_isbn:
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    sql = """SELECT
                 [ISBN]
                 FROM [borrow]
                 WHERE [ISBN]='{}'
    """.format(isbn)
    rs.Open(sql, conn, 1, 1)
    book_count.append((isbn, rs.RecordCount))

conn.Close()
# print(book_count)

book_count = sorted(book_count, key = lambda x : x[1], reverse=True)
# print(book_count)
for i in range(3):
    print(book_count[i])
