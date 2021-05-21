import win32com.client


mdb_file = "Database.accdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

sql = """CREATE TABLE book(
            ISBN    VARCHAR(17) NOT NULL,
            书名     VARCHAR(200),
            作者     VARCHAR(100),
            类型     VARCHAR(8),
            出版日期  VARCHAR(10),
            数量     INT DEFAULT 0,
            PRIMARY KEY (ISBN))"""
conn.Execute(sql)  # 创建表[book]
sql = """CREATE TABLE student(
            学号 VARCHAR(5) NOT NULL,
            密码 VARCHAR(20),
            姓名 VARCHAR(20),
            性别 VARCHAR(2),
            年龄 INT DEFAULT 0,
            年级 VARCHAR(4),
            班级 VARCHAR(2),
            PRIMARY KEY (学号))"""
conn.Execute(sql)  # 创建表[student]
sql = """CREATE TABLE borrow(
            id      INT NOT NULL,
            学号     VARCHAR(5),
            ISBN    VARCHAR(17),
            借阅日期 VARCHAR(10),
            PRIMARY KEY (id))"""
conn.Execute(sql)  # 创建表[borrowt]
sql = """ALTER TABLE [borrow] 
            ALTER COLUMN [id] COUNTER (1, 1)"""
conn.Execute(sql)  # 设置表[borrow]字段[id]为自动编号

conn.Close()
