import pyodbc
import os

accdb_file = """{}\Database.accdb""".format(os.getcwd())  # 数据库文件
driver = """{Microsoft Access Driver (*.mdb, *.accdb)}"""  # 驱动程序，在用户DSN配置上述accdb文件
conn = pyodbc.connect("""Driver={};DBQ={}""".format(driver, accdb_file))  # 连接数据库文件

cursor = conn.cursor()  # 为数据库创建游标对象

sql = """SELECT
             TOP 8
             [ISBN],
                 (SELECT [书名] FROM [book] WHERE [ISBN]=[borrow].[ISBN]) AS [书名],
                 COUNT(*) AS [借阅数量]
             FROM [borrow]
             GROUP BY [ISBN]
             ORDER BY COUNT(*) DESC
"""  # 查询语句
cursor.execute(sql)  # 将数据缓存到游标对象中
# cursor.commit()  # 向数据库服务器提交数据，当使用INSERT、UPDATE、DELETE等写操作命令时需要执行！

data = cursor.fetchall()  # 将查询结果放到自定义的变量中,数据类型：列表，每个元素为一条记录
if data:
    for item in data:  # 遍历每个元素
        print(item)  # 打印元素，每条记录为一个元组

cursor.close()  # 关闭游标
conn.close()  # 关闭数据库连接
