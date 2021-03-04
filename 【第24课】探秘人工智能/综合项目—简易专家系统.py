def jizhui():
    j = input("该动物是脊椎动物吗？（y/n）")
    if j == 'y':
        yumao()
    elif j == 'n':
        ke()
    else:
        print("输入错误！")


def ke():
    k = input("该动物有壳吗？（y/n）")
    if k == 'y':
        print("该动物是河蚌！")
    elif k == 'n':
        print("该动物是蚯蚓！")
    else:
        print("输入错误！")


def yumao():
    k = input("该动物有羽毛吗？（y/n）")
    if k == 'y':
        print("该动物是鸟！")
    elif k == 'n':
        tui()
    else:
        print("输入错误！")


def tui():
    k = input("该动物有腿吗？（y/n）")
    if k == 'y':
        print("该动物是青蛙！")
    elif k == 'n':
        print("该动物是鱼！")
    else:
        print("输入错误！")


jizhui()
