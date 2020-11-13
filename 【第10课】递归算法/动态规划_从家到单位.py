# 小赵从家(0,0)出发去单位(4,3)上班要经过多条街道，假如他只能向西或向南行走，则他上班有多少种不同的走法？

def find_walk_num(x, y):
    if y == 0:
        if x == 1:
            return 1
        return find_walk_num(x - 1, 0)
    if x == 0:
        if y == 1:
            return 1
        return find_walk_num(0, y - 1)
    return find_walk_num(x - 1, y) + find_walk_num(x, y - 1)


result = find_walk_num(4, 3)
print("从家(0,0)到单位(4,3)的走法共有：{}种".format(result))
