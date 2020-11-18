# 直接插入排序
def inert_sort(lst):
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            tmp = lst[i]
            seq = i
            while seq > 0 and lst[seq-1] > tmp:
                lst[seq] = lst[seq-1]
                seq -= 1
            lst[seq] = tmp
    return lst


# 冒泡排序
def bubble_sort(lst):
    lst_len = len(lst)
    # 控制循环次数，N个元素需要N轮比较
    for i in range(lst_len - 1):
        # 第n个元素需要比较(N-n-1)次
        for j in range(lst_len - i - 1):
            if lst[j] > lst[j + 1]:
                # 如果第j个元素大于j+1,则交换
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# 鸡尾酒排序
def cocktail_sort(lst):
    size = len(lst)
    sign = 1
    for i in range(int(size / 2)):
        if sign:
            sign = 0
            for j in range(i, size - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
            for k in range(size - 2 - i, i, -1):
                if lst[k] < lst[k - 1]:
                    lst[k], lst[k - 1] = lst[k - 1], lst[k]
                    sign = 1
        else:
            break
    return lst


# 归并排序
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    num = int(len(lst) / 2)
    left = merge_sort(lst[:num])
    right = merge_sort(lst[num:])
    return merge(left, right)


def merge(left, right):
    r_lenth, l_lenth = 0, 0
    result = []
    while l_lenth < len(left) and r_lenth < len(right):
        if left[l_lenth] <= right[r_lenth]:
            result.append(left[l_lenth])
            l_lenth += 1
        else:
            result.append(right[r_lenth])
            r_lenth += 1
    result += list(left[l_lenth:])
    result += list(right[r_lenth:])
    return result


# 直接选择排序
def selection_sort(lst):
    arr = lst[:]
    newlst = []  # 定义新生成数组的类型以及分配内存空间
    for i in range(len(arr)):
        smallest, smallest_index = findsmallest(arr)
        newlst.append(smallest)  # 将每次得到的最小元素加在数组后面
        arr.pop(smallest_index)  # 删除原数组中已经被查找出来的最小元素
    return newlst


def findsmallest(lst):  # 找出数组中最小元素的函数
    smallest = lst[0]  # 将arr数组中的第一个元素作为最小值的初始化值
    smallest_index = 0  # 对应上行代码，初始化存储最小元素的索引
    for i in range(1, len(lst)):  # 从数组中第二个元素开始遍历
        if smallest > lst[i]:
            smallest = lst[i]
            smallest_index = i
    return smallest, smallest_index


# 堆排序
def heap_sort(lst):  # 无序区大根堆排序
    first = len(lst) // 2 - 1
    for start in range(first, -1, -1):
        # 从下到上，从左到右对每个节点进行调整，循环得到非叶子节点
        big_endian(lst, start, len(lst)-1)  # 去调整所有的节点
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]  # 顶部尾部互换位置
        big_endian(lst, 0, end - 1)  # 重新调整子节点的顺序，从顶开始调整
    return lst


def big_endian(lst, start, end):
    root = start
    child = root * 2 + 1  # 左孩子
    while child <= end:
        # 孩子比最后一个节点还大，也就意味着最后一个叶子节点了，就得跳出去一次循环，已经调整完毕
        if child + 1 <= end and lst[child] < lst[child + 1]:
            # 为了始终让其跟子元素的较大值比较，如果右边大就左换右，左边大的话就默认
            child += 1
        if lst[root] < lst[child]:
            # 父节点小于子节点直接交换位置，同时坐标也得换，这样下次循环可以准确判断：是否为最底层，
            # #是不是调整完毕
            lst[root], lst[child] = lst[child], lst[root]
            root = child
            child = root * 2 + 1
        else:
            break


if __name__ == "__main__":
    import numpy as np
    import time
    a = list(np.random.randint(1, 1000000, 6000))
    t0 = time.time()
    answer = sorted(a)
    t1 = time.time()
    print("原序列前十项:{}".format(a[:10]))
    print("新序列前十项:{} 用时：{}秒".format(answer[:10], t1 - t0))
    # 算法字典
    fun_list = {
        "inert_sort": "插入法排序",
        "bubble_sort": "冒泡法排序",
        "cocktail_sort": "鸡尾酒排序",
        "merge_sort": "归并排序",
        "selection_sort": "直接选择排序",
        "heap_sort": "堆排序",
    }
    for key, value in fun_list.items():
        t0 = time.time()
        b = eval(key)(a)
        t1 = time.time()
        if b == answer:
            print("{}用时 {:0.8f} 秒".format(value, t1 - t0))
        else:
            print("{}新序列:[{} {} ……{} {}] 错误".format(value, b[0], b[1], b[-2], b[-1]))

input("运行完毕，请按回车键退出...")
