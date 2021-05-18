import win32com.client


books_data = [
    ('978-7-1153-0972-3', '宇宙之书——从托勒密、爱因斯坦到多重宇宙', '约翰·D.巴罗', '科普', '2014-04-03', 10),
    ('978-7-3024-0433-0', '山海经', '孙见坤', '文学', '2015-11-01', 4),
    ('978-7-5379-6326-8', '中国的地形·壮美画卷', '贾文毓', '地理', '2015-02-01', 10),
    ('978-7-5624-9236-8', '天文之书', '吉姆·贝尔', '科普', '2015-10-25', 8),
    ('978-7-5193-0020-3', '中国通史“慢读”系列', '吕思勉', '历史', '2016-02-01', 10),
    ('978-7-5143-4589-6', '力学原来这么有趣！', '大井喜久夫', '科普', '2016-05-01', 15),
    ('978-7-1001-1969-6', '西游记', '吴承恩', '小说', '1980-1-1', 9),
    ('978-7-0200-0872-8', '三国演义', '罗贯中', '小说', '1998-1-1', 3),
    ('978-7-5533-2335-0', '资治通鉴', '司马光', '历史', '2000-1-1', 5),
    ('978-7-5039-3471-1', '孙中山传', '尚明轩', '人物', '2008-3-1', 3),
    ('978-7-5499-8387-2', '教育写作', '颜莹', '教育', '2020-3-1', 9)
    ]

mdb_file = "图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

for data in books_data:
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    sql = """SELECT ISBN FROM books
             WHERE ISBN='{}'""".format(data[0])
    rs.Open(sql, conn, 1, 1)

    if rs.EOF:
        sql = """INSERT INTO books (ISBN,书名,作者,种类,出版日期,数量)
                 VALUES {}""".format(data)
    else:
        sql = """UPDATE books
                 SET 数量=数量+{}
                 WHERE ISBN='{}'""".format(data[-1], data[0])   # 更新

    conn.Execute(sql)  # 执行sql语句

conn.Close()
