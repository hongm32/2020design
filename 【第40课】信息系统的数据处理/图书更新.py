import win32com.client


mdb_file = "图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

sql = "UPDATE books SET 数量=数量-1 WHERE ISBN='978-7-0200-0872-8'"
"""UPDATE命令格式：
      DELETE 表名 SET 字段=值 WHERE 条件
其中，WHERE条件为可选项：
  当WHERE条件存在时，UPDATE将修改指定表中符合条件的记录；
  当WHERE条件不存在时，将修改指定表中所有数据。
"""
conn.Execute(sql)  # 执行sql语句

conn.Close()
