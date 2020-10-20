# 4.1.2：P090-寻找被删的ID号代码
# 说明：异或应用于逻辑运算，其运算法则为：
# 0 ^ 0 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1, 1 ^ 1 = 0
# 由于两个相同数异或结果为0，而任何数异或0的结果等于数据本身。
# 因此，可以把文件中所有ID号直接进行异或，只出现一次的数据就能被找出，并且最后出现的异或结果就是这个数。
target = 0  # 设置初始值

f1 = open("copy.txt")  # 打开备份文件
li = f1.readlines()  # 读取每行数据
for line in li:
    target = target ^ int(line)  # 将读取的数据做异或运算
f1.close()  # 关闭备份文件
f2 = open("trouble.txt")  # 打开故障文件
li = f2.readlines()  # 读取每行数据
for line in li:
    target = target ^ int(line)  # 将读取的数据做异或运算
f2.close()  # 关闭故障文件
print("被删除的ID号是:", target)  # 输出被删除的ID号
input("运行完毕，请按回车键退出...")
