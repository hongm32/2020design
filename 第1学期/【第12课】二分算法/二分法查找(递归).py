def search(array, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] > target:
            return search(array, low, mid - 1, target)
        else:
            return search(array, mid + 1, high, target)
    else:
        return -1  # 表示没有找到


a = list(range(1000))
x = int(input("请输入要查找的1000以内的整数:"))
index = search(a, 0, 1000, x)
print("查找元素在第{}个".format(index))
input("运行完毕，请按回车键退出...")
