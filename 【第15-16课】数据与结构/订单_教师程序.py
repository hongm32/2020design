queue_list = []                        # 定义列表queue_list存储订单
x = 0
while x != 4:                      # 当x=!4时，执行循环
    print('1. 添加订单')
    print('2. 发货')
    print('3. 查看订单列表')
    print('4. 退出')
    x = int(input("输入你的选择:"))  # 输入选择项
    if x == 1:
        y = input("输入订单编号:")  # 输入订单编号
        queue_list.append(y)         # 在列表queue_list中添加订单号
    elif x == 2:
        if len(queue_list) == 0:       # 如果订单列表为空
            print("订单列表为空")
        else:
            print("发货单号:" + queue_list.pop(0))
    elif x == 3:
        print("等待发货:", queue_list)            # 查询列表queue_list中的订单号
    print()
  
input("运行完毕，请按回车键退出...")
