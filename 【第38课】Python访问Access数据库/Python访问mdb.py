import win32com.client


mdb_file = "图书借阅管理.mdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
try:
    DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007以前版本
    conn.Open(DSN)  # 用游标打开数据连接
except:
    DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后版本
    conn.Open(DSN)  # 用游标打开数据连接


# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
sql = 'books'
# sql = "SELECT * FROM books"
rs.Open(sql, conn, 1, 1)
# Open(Source,ActiveConnection,CursorType,LockType,Options)说明：
# Source:数据表
# ActiveConnection：Recordset对象，可以是一个Connection对象或是一串包含数据库连接信息（ConnectionString）的字符串参数。
# CursorType：表示将以什么样的游标类型启动数据, 包括：
#     0 adOpenForwardOnly 缺省值，启动一个只能向前移动的游标，
#     1 adOpenKeyset 启动一个Keyset类型的游标，
#     2 adOpenDynamic 启动一个Dynamic类型的游标。
#     3 adOpenStatic 启动一个Static类型的游标
# LockType：表示要采用的Lock类型，包含
#     1 adLockReadOnly 缺省值，Recordset对象以只读方式启动，无法运行AddNew、Update及Delete等方法
#     2 adLockPrssimistic 当数据源正在更新时，系统会暂时锁住其他用户的动作，以保持数据一致性。
#     3 adLockOptimistic 当数据源正在更新时，系统并不会锁住其他用户的动作，其他用户可以对数据进行增、删、改的操作。
#     4 adLockBatchOptimistic 当数据源正在更新时，其他用户必须将CursorLocation属性改为adUdeClientBatch才能对数据进行增、删、改的操作。　

# 光标移到首条记录
rs.MoveFirst()
"""记录集对象的方法： 
rs.MoveNext 将记录指针从当前的位置向下移一行 
rs.MovePrevious 将记录指针从当前的位置向上移一行 
rs.MoveFirst 将记录指针移到数据表第一行 
rs.MoveLast 将记录指针移到数据表最后一行 
rs.AbsolutePosition=N 将记录指针移到数据表第N行 
rs.AbsolutePage=N 将记录指针移到第N页的第一行 
rs.PageSize=N 设置每页为N条记录 
rs.PageCount 根据 pagesize 的设置返回总页数 
rs.RecordCount 返回记录总数 
rs.BOF 返回记录指针是否超出数据表首端，true表示是，false为否 
rs.EOF 返回记录指针是否超出数据表末端，true表示是，false为否 
rs.Delete 删除当前记录，但记录指针不会向下移动 
rs.AddNew 添加记录到数据表末端
rs.Update 更新数据表记录
rs.GetRows 获取行数据元组"""

# 遍历记录，读取数据
while not rs.EOF:
    for i in range(rs.Fields.Count):
        print('{}: {}'.format(rs.Fields[i].Name, rs.Fields[i].Value))    # 字段名：字段内容
    print(end='\n')
    rs.MoveNext()  # 光标移到下条记录

print('该表有{}个字段'.format(rs.Fields.Count))
print('该表有{}条记录'.format(rs.RecordCount))


# 关闭连接
conn.Close()
