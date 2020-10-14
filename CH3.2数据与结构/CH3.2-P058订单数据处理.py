listque = []  # 定义列表listque存储订单
x = 0
while x != 4:  # 当x=!4时，执行循环
    print('\n1. 添加订单')
    print('2. 发货')
    print('3. 查看订单列表')
    print('4. 退出')
    x = int(input("输入你的选择:"))  # 输入选择项
    if x == 1:
        y = input("输入订单编号:")  # 输入订单编号
        listque.append(y)  # 在列表listque中添加订单号
    elif x == 2:
        if len(listque) == 0:  # 如果订单列表为空
            print("订单列表为空")
        else:
            print("发货单号:" + listque.pop(0))
    elif x == 3:
        print("等待发货:", listque)  # 查询列表listque中的订单号
