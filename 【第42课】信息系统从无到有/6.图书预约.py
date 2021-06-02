import win32com.client
import time


def login():
    """学生登录"""
    while True:
        student_number = input("输入学号：")
        if not student_number:
            print("学号输入无效！")
            continue
        # 查询语句
        rs = win32com.client.Dispatch(r'ADODB.Recordset')
        sql = """SELECT
                     学号,密码
                     FROM student
                     WHERE 学号='{}'""".format(student_number)
        rs.Open(sql, conn, 1, 1)
        if rs.EOF:
            print("该学号不存在！")
        else:
            data = rs.GetRows()
            break

    step = 4
    while step > 0:
        student_password = input("输入密码：")
        # 判断查询结果中的密码和输入的密码是否一致
        for index, passwd in enumerate(data[1]):
            if student_password == passwd:
                return student_number  # 登陆成功，返回学号
        step -= 1
        print("密码错误！还可再试{}次".format(step))
    return False


def show():
    # 查询可借阅图书
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    sql = """SELECT
                 ISBN,书名
                 FROM [book]
                 WHERE 数量>0"""
    book_name = input("输入你想要预约的图书书名：")
    if book_name:
        sql += """ AND 书名 LIKE '%{}%'""".format(book_name)
    book_auth = input("输入你想要预约的图书作者：")
    if book_auth:
        sql += """ AND 作者 LIKE '%{}%'""".format(book_auth)
    rs.Open(sql, conn, 1, 1)

    if rs.RecordCount:
        print('查询到{}本书：'.format(rs.RecordCount))
        records = rs.GetRows()
        for idx, name in enumerate(records[1]):
            print("  {}:{}".format(idx, name))
        print("  e: 退出")
        select = input("选择你要预约的书名编号：")
        if select.isdigit() and int(select) <= len(records[0]):
            return records[0][int(select)]
        elif select.lower() == "q":
            exit()
    return False


def modify():
    """预约图书并更新可借阅图书数量"""
    try:
        # 更新图书数量
        sql_update = """UPDATE book
                            SET [数量]=[数量]-1
                            WHERE ISBN='{}'""".format(select_isbn)
        conn.Execute(sql_update)  # 执行sql语句
        # 将预约信息插入借阅表
        today = time.strftime('%Y-%m-%d ', time.localtime(time.time()))  # 获取当前日期，作为借阅日期
        sql_insert = """INSERT INTO borrow (学号,ISBN,借阅日期)
                            VALUES ('{}','{}','{}')""".format(student_number,
                                                              select_isbn,
                                                              today)
        conn.Execute(sql_insert)
    except BaseException:
        return False
    return True


def not_borrow():
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    sql = """SELECT *
                 FROM borrow
                 WHERE ISBN='{}' AND 学号='{}'""".format(select_isbn,
                                                       student_number)
    rs.Open(sql, conn, 1, 1)
    return rs.EOF


def show_borrow():
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    sql = """SELECT
                 (SELECT 书名 FROM book WHERE ISBN=borrow.ISBN) as 书名
                 FROM borrow WHERE 学号='{}'""".format(student_number)
    rs.Open(sql, conn)
    print("你已借图书：")
    while not rs.EOF:
        for i in range(rs.Fields.Count):
            print('  {}'.format(rs.Fields[i].Value))    # 字段名：字段内容
        # print(end='\n')
        rs.MoveNext()  # 光标移到下条记录


if __name__ == "__main__":
    mdb_file = "Database.accdb"  # 数据库文件
    conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
    DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
    conn.Open(DSN)  # 用游标打开数据连接

    student_number = login()
    if student_number:
        while True:
            show_borrow()
            select_isbn = show()
            if select_isbn:
                if not_borrow():
                    if modify():
                        print("  预约成功！")
                    else:
                        print("  预约失败！")
                else:
                    print("你已借了本书，不要重复！")
            else:
                print("查无此书，无法预约！")
            flag = input("是否继续(Y/N)：")
            if flag.lower() != "y":
                break

    conn.Close()
