import win32com.client

tablename = "books"
conn = win32com.client.Dispatch(r"ADODB.Connection")
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = 图书借阅管理.mdb'  # Access2007及以后
conn.Open(DSN)

sql = "DELETE FROM books WHERE 书名='教育写作'"
"""DELETE命令格式：
      DELETE FROM 表名 WHERE 条件
其中，WHERE条件为可选项：
  当WHERE条件存在时，DELETE将删除表中符合条件的记录；
  当WHERE条件不存在时，将删除表中所有数据。
需要注意的是，删除表中所有数据后，表仍然慧，但肯中数据不可恢复！
"""
conn.Execute(sql)  # 执行sql语句

conn.Close()
