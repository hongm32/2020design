import random
import win32com.client


data = [[], []]
for idx in range(2):
    with open(f"name_{idx}.txt", "r", encoding="UTF-8") as f:
        for line in f:
            line = line.replace("\n", "")
            if line:
                data[idx].append(line)

mdb_file = "Database.accdb"  # 数据库文件
conn = win32com.client.Dispatch(r"ADODB.Connection")  # 建立连接对象
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = {}'.format(mdb_file)  # Access2007及以后
conn.Open(DSN)  # 用游标打开数据连接

sql = """INSERT INTO student (学号,密码,姓名,性别,年龄,年级,班级)
                 VALUES {}"""

for nj, grade in enumerate(["高一", "高二", "高三"]):
    for bj in range(1, 13):
        count = random.randint(54, 60)
        for idx in range(1, count + 1):
            info = []
            number = str(nj + 1) + str(bj).zfill(2) + str(idx).zfill(2)
            info.append(number)
            info.append("1943")  # 简化，统一密码1943
            sex = random.randint(0, 1)  # 性别，0：女 1：男
            if sex == 1:
                sex_info = "男"
            else:
                sex_info = "女"
            name = data[sex].pop()
            # info.extend([name, sex_info])
            info.append(name)
            info.append(sex_info)
            info.append(nj + random.randint(16, 17))
            info.extend([grade, str(bj).zfill(2)])
            conn.Execute(sql.format(tuple(info)))
            
conn.Close()
            
    
