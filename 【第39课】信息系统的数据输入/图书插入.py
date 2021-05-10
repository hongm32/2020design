import win32com.client

tablename = "books"
conn = win32com.client.Dispatch(r"ADODB.Connection")
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = 图书借阅管理.mdb'  # Access2007及以后
conn.Open(DSN)

sql = "INSERT INTO books (ISBN,书名,作者,类型,出版时间,数量) VALUES ('978-7-5499-8387-2','教育写作','颜莹','教育','202-3-1',9)"
conn.Execute(sql)  # 执行sql语句

conn.Close()
