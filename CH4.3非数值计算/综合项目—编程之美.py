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


if __name__ == "__main__":
    import numpy as np
    import time
    a = np.random.randint(1, 1000000, 8000)
    print("原序列前十项:{}".format(a[:10])) 
    t1 = time.time()
    b = inert_sort(a)
    t2 = time.time()
    print("新序列:[{} {} ……{} {}]".format(b[0], b[1], b[-2], b[-1]))    
    print("插入法用时 {:0.8f} 秒".format(t2-t1))    
    c = bubble_sort(a)
    t3 = time.time()
    # print("新序列:[{} {} …… {} {}]".format(c[0], c[1], c[-2], c[-1]))
    print("冒泡法用时 {:0.8f} 秒".format(t3-t2))
