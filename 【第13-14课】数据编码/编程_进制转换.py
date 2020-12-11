while True:
    flag = 0
    while True:
        num = input('请输入要转换进制的任意进制整数：')
        if num.upper() in ["Q", "E", "EXIT", "QUIT"]:
            exit()
        if num.isdecimal():
            flag = 10
            break
        if num[:2].upper() in ["0X", "0B", "0O"]:
            num_list = None
            if num[:2].upper() == "0X":
                num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
                flag = 16
            if num[:2].upper() == "0B":
                num_list = ['0', '1']
                flag = 2
            if num[:2].upper() == "0O":
                num_list = ['0', '1', '2', '3', '4', '5', '6', '7']
                flag = 8
            if sum([True for i in num[2:] if i.upper() in num_list]) == len(num) - 2:
                break
            else:
                print("输入的格式不符！")
    num_dec = int(num, flag)
    num_bin = bin(num_dec)
    num_oct = oct(num_dec)
    num_hex = hex(num_dec)
    print('{}进制{}转成十进制(整形)为：{}'.format(flag, num, num_dec))
    print('{}进制{}转成二进制(字符)为：{}'.format(flag, num, num_bin))
    print('{}进制{}转成八进制(字符)为：{}'.format(flag, num, num_oct))
    print('{}进制{}转成十六进制(字符)为：{}'.format(flag, num, num_hex))
    # print(type(num), type(num_dec), type(num_bin), type(num_oct), type(num_hex))
