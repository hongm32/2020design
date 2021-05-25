import random
import win32com.client
import time


def not_borrow():
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    sql = """SELECT * 
                 FROM borrow 
                 WHERE ISBN='{}' AND 学号='{}'""".format(select_isbn, student_number)
    rs.Open(sql, conn, 1, 1)
    return rs.EOF


def modify():
    """预约图书并更新可借阅图书数量"""
    # 更新图书数量
    sql_update = """UPDATE book 
                        SET [数量]=[数量]-1 
                        WHERE ISBN='{}'""".format(select_isbn)
    conn.Execute(sql_update)  # 执行sql语句
    # 将预约信息插入借阅表
    today = time.strftime('%Y-%m-%d ', time.localtime(time.time() - random.randint(0, 10) * 86400))  # 获取当前日期-RANDOM，作为借阅日期
    sql_insert = """INSERT INTO borrow(学号,ISBN,借阅日期) 
                        VALUES ('{}','{}','{}')""".format(student_number,
                                                          select_isbn,
                                                          today)
    conn.Execute(sql_insert)

    return True


mdb_file = "Database.accdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

sql = """CREATE TABLE borrow(
            id      INT NOT NULL,
            学号     VARCHAR(5),
            ISBN    VARCHAR(17),
            借阅日期 VARCHAR(10),
            PRIMARY KEY (id))"""
try:
    conn.Execute(sql)  # 创建表[borrow]
except:
    conn.Execute("""DROP TABLE [borrow]""")  # 删除表[borrow]
    conn.Execute(sql)  # 创建表[borrowt]
sql = """ALTER TABLE [borrow] 
            ALTER COLUMN [id] COUNTER (1, 1)"""
conn.Execute(sql)  # 设置表[borrow]字段[id]为自动编号

for i in range(200):
    nj = random.randint(1, 3)
    bj = random.randint(1, 12)
    idx = random.randint(1, 54)
    student_number = str(nj) + str(bj).zfill(2) + str(idx).zfill(2)
    print("学生{}开始预约".format(student_number))
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    sql = """SELECT 学号,密码 
                 FROM student 
                 WHERE 学号='{}'""".format(student_number)
    rs.Open(sql, conn, 1, 1)
    if rs.RecordCount:
        rs = win32com.client.Dispatch(r'ADODB.Recordset')
        sql = """SELECT ISBN 
                     FROM book 
                     WHERE 数量>0"""
        rs.Open(sql, conn, 1, 1)
        book_info = list(rs.GetRows()[0])
        select_isbn = random.choice(book_info)
        if not_borrow():
            print("  准备预约图书ISBN：{}".format(select_isbn))
            if modify():
                print("  预约成功！")
            else:
                print("  预约失败！")
        else:
            print("  你已借了本书，不要重复！")
    else:
        print("  查无此人{}！".format(student_number))

conn.Close()
