import csv
import random


student = [[] for _ in range(12)]  # 生成班级学号空列表
student_dict = {}  # 生成学生信息空字典
with open('20021.csv', encoding="UTF-8") as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        student[int(row[4][5:7]) - 1].append(row[4])
        student_dict[row[4]] = row
while True:
    try:
        bj = int(input("输入班级(1-12)："))
    except NameError and ValueError:
        print("班级输入错误，请重新输入")
    else:
        if 1 <= bj <= 12:
            break
while True:
    luck = random.choice(student[bj - 1])
    print()
    print("恭喜！高一({:0>2})班本次点名回答问题的同学是：{}{}".format(bj, luck[-2:], student_dict[luck][3]))
    if input().lower() == "q":
        break
input("程序运行结束，按回车键退出···")
