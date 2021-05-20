import win32com.client

mdb_file = "../【第37课】数据库的构建/图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

sql = "DELETE FROM books"
"""DELETE命令格式：
      DELETE FROM 表名 WHERE 条件
其中，WHERE条件为可选项：
  当WHERE条件存在时，DELETE将删除表中符合条件的记录；
  当WHERE条件不存在时，将删除表中所有数据。
需要注意的是，删除表中所有数据后，表仍然慧，但肯中数据不可恢复！
"""
conn.Execute(sql)  # 执行sql语句

conn.Close()
