import win32com.client


mdb_file = "../【第37课】数据库的构建/图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
# 查询语句
sql = """SELECT
             *
             FROM [books]
             WHERE [数量]<5 OR [类型]='教材'"""
rs.Open(sql, conn, 1, 1)
"""查询命令基本格式：
    SELECT 
        字段列表 
        FROM 表名
        WHERE 条件
说明：1、字段列表，可使用通配符*，表示所有字段
     2、WHERE子句可选，如果存在多个条件，可用AND和OR连接，如
    SELECT
        *
        FROM [books]
        WHERE [数量]<5 OR [类型]='教材'
模糊查询：SELECT WHERE LIKE
      3、LIKE连接：使用通配符来代替字符：%表示0或任意多个，_表示1个，如
    SELECT
        *
        FROM [books]
        WHERE [作者] LIKE '李%'
TOP子句：
    SELECT
        TOP 2
        *
        FROM [book]  # 表示选择前2条记录
    SELECT
        TOP 2 PERCENT 
        *
        FROM [book]  # 表示选择前2%的记录
ORDER BY子句：
    SELECT 
        TOP 2 
        * 
        FROM [book] 
        ORDER BY [书名] DESC  # 表示按书名排序，DESC表示降序
聚合查询：
    1、常与SELECT的GROUP BY子句一同使用
    2、常用的聚合函数：
        COUNT()  # 计数函数
        MAX()    # 最大值函数
        MIN()    # 最小值函数
        SUM()    # 求和函数
        AVG()    # 求平均值函数，如
    SELECT 
        TOP 4 
        ISBN,
            COUNT(*) AS [借阅数量] 
        FROM [borrow] 
        GROUP BY ISBN 
        ORDER BY COUNT(*) DESC
多表查询：
    SELECT 
        borrow.学号,
            student.姓名,
            borrow.ISBN,
            books.书名 
        FROM books,borrow,student 
        WHERE borrow.学号=student.学号 AND borrow.ISBN=books.ISBN
"""

print('查询到{}条记录：\n'.format(rs.RecordCount))
# 遍历记录，读取数据
# rs.MoveFirst()  #光标移到首条记录
while not rs.EOF:
    for i in range(rs.Fields.Count):
        print('  {}: {}'.format(rs.Fields[i].Name, rs.Fields[i].Value))    # 字段名：字段内容
    print(end='\n')
    rs.MoveNext()  # 光标移到下条记录

conn.Close()
