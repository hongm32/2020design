# 4.1.2：P090-寻找被删的ID号代码
sum1 = 0  # 设置初始值
sum2 = 0  # 设置初始值
f1 = open("copy.txt")  # 打开备份文件
li = f1.readlines()  # 读取每行数据
for line in li:
    sum1 = sum1 + int(line)  # 将读取的数据做和运算
f1.close()  # 关闭备份文件
f2 = open("trouble.txt")  # 打开故障文件
li = f2.readlines()  # 读取每行数据
for line in li:
    sum2 = sum2 + int(line)  # 将读取的数据做和运算
f2.close()  # 关闭故障文件
print("被删除的ID号是:", sum1 - sum2)  # 输出被删除的ID号
input("运行完毕，请按回车键退出...")
