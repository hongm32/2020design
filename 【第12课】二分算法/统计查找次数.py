print('''假设一本字典有1000页，老师藏了一条秘密信息在其中一页。
现在通过运行程序找到相应页码中的这条信息！
并告诉我你用几次找到的？
你有机会获得一个惊喜！！''')
set_number = 328  # 设定正确的数
number_min = 1
number_max = 1000
times = 0
for times in range(10):
    try:
        guess_number = int(input("请输入查找页数({}-{})：".format(number_min, number_max)))
    except NameError and ValueError:
        guess_number = -1
    if guess_number == -1:
        print("输入内容必须为整数！")
    elif guess_number > set_number:
        print("很遗憾，页数大了")
        number_max = guess_number - 1
    elif guess_number < set_number:
        print("抱歉，页数小了")
        number_min = guess_number + 1
    else:
        print("翻了{}次，被你找到啦！".format(times + 1))
        print("不要关闭！！！")
        print("联系老师会有surprise")        
        break
else:
    print("翻了{}次还未找到！".format(times + 1))
input()
