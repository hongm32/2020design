import win32com.client
import time


mdb_file = "Database.accdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接


# 学生登陆[student]
while True:
    student_number = input("输入你的学号：")
    sql = """SELECT
                 [学号],[密码],[姓名]
                 FROM [student]
                 WHERE [学号]='{}'
          """.format(student_number)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs.Open(sql, conn, 1, 1)
    if rs.EOF:
        print("该学号不存在！")
    else:
        data = rs.GetRows()
        break

step = 4
while step > 0:
    step -= 1
    student_passwd = input("输入密码：")
    for index, passwd in enumerate(data[1]):
        if passwd == student_passwd:
            student_name = data[2][index]
            print("欢迎 ({}){} 登陆图书借阅系统".format(
                student_number,
                student_name))
            break
    else:
        print("密码错误！还可再试{}次".format(step))
        continue
    break


# 显示学生已借图书
sql = """SELECT
             [ISBN],
             (SELECT [书名] FROM [book] WHERE [ISBN]=[borrow].[ISBN]) AS [书名]
             FROM [borrow]
             WHERE [学号]='{}'
      """.format(student_number)
rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs.Open(sql, conn, 1, 1)
if rs.EOF:
    print("  你未借书！")
else:
    print("你已借图书：")
    data = rs.GetRows()
    for index, title in enumerate(data[1]):
        print("  {} {}".format(index + 1, title))


# 查询能借(库存数量大于0)的图书[book]
sql = """SELECT
             [ISBN],[书名]
             FROM [book]
             WHERE [数量]>0
      """
print("查询可借阅图书：")
name = input("  输入你想预约图书的书名：")
if name:
    sql += """ AND [书名] LIKE '%{}%'""".format(name)
auth = input("  输入你想预约图书的作者：")
if auth:
    sql += """ AND [作者] LIKE '%{}%'""".format(auth)
rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs.Open(sql, conn, 1, 1)
if rs.EOF:
    print("查无此书！")
else:
    print("查询到以下图书：")
    data = rs.GetRows()
    for index, name in enumerate(data[1]):
        print("  {} {}".format(index, name))
    choice = input("选择图书编号：")
    if choice.isdigit() and int(choice) < len(data[1]):
        index = int(choice)
        book_isbn = data[0][index]
        book_name = data[1][index]
    else:
        print("编号输入错误！")


# 添加借书记录[borrow]
today = time.strftime('%Y-%m-%d ', time.localtime(time.time()))  # 获取当前日期，作为借阅日期
sql = """INSERT INTO [borrow] ([学号],[ISBN],[借阅日期])
                            VALUES ('{}','{}','{}')
      """.format(student_number,
                 book_isbn,
                 today)
a = conn.Execute(sql)


# 更新库存数量[book]
sql = """UPDATE [book]
             SET [数量]=[数量]-1
             WHERE [ISBN]='{}'
      """.format(book_isbn)
b = conn.Execute(sql)

print("预约成功！")
print(a, b)
