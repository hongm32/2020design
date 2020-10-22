def fun(num):
    s = 0
    i = 0
    while s < num:
        i = i + 1
        s = s + 1 / i
    return i, s


print('这是一个有关求1+1/2+1/3+1/4+……+1/n值不小于常数k的最小n的程序')
try:
    k = float(input("请输入常数k的值(建议不要超过15)："))
except NameError and ValueError:
    print("必须输入一个数值！")
else:
    if k < 1:
        print("你输入的k值太小, 式子没有意义！")
    elif k <= 15:
        print("最小n值为:", fun(k)[0], "此时和为", fun(k)[1])
    elif k <= 710.3:
        print("你输入的k值太大, 估算n值约为{:0,.0f}".format(2.718281828459045 ** (k - 0.577215664901532)))
    else:
        print("你输入的k值太大, 超过Python最大数值范围，无法计算！")
input("运行完毕，请按回车键退出...")
