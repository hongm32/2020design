# 先要安装与Python和操作系统匹配的pywin32
# 利用win32com.client模块的COM组件访问功能，通过ADODB访问Access的mdb文件
# 建立数据库连接
import win32com.client
conn = win32com.client.Dispatch(r"ADODB.Connection")
# DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = 旅行小助手.mdb'  # Access2007以前
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = 旅行小助手.mdb'  # Access2007及以后
conn.Open(DSN)

# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')
tablename = '旅行线路表'
rs.Open('[' + tablename + ']', conn, 1, 3)

# 遍历记录，读取数据
# rs.MoveFirst()  #光标移到首条记录
while not rs.EOF:
    for i in range(rs.Fields.Count):
        print(rs.Fields[i].Name, ":", rs.Fields[i].Value)    # 字段名：字段内容
    print(end='\n')
    rs.MoveNext()  # 光标移到下条记录
print('该表有'+str(rs.Fields.Count)+'个字段')
print('该表有'+str(rs.RecordCount)+'条记录')

# 关闭连接
conn.Close()
