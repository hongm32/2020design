que_list = []  # 定义列表que_list存储停车状况
max_volume = 8  # 停车位最大容量
while True:  # 永远执行循环
    print('\n1. 进栈停车')  # \n表示换行打印
    print('2. 开车出栈')
    print('3. 查看停车库')
    print('其他. 退出')
    x = input("输入你的选择:")  # 输入选择项
    if x == '1':
        if len(que_list) < max_volume:
            print("还有" + str(max_volume - len(que_list)) + "个停车位。")  # 输出空余停车位
            que_list.append(input("请输入进栈停车车牌:"))  # 在列表中添加停车车牌
        else:
            print("对不起，停车位已满。")
    elif x == '2':
        if len(que_list) == 0:  # 如果停车库为空
            print("停车库为空。")
        else:
            print(que_list.pop() + "开出。")  # 删除列表尾元素，表示开车出栈
    elif x == '3':
        print(que_list)  # 查看停车库
    else:
        break  # 退出循环
