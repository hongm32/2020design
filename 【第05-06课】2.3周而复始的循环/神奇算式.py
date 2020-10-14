print("""
问题：神奇算式
　　由4个不同的数字,组成的一个乘法算式,它们的乘积仍然由这4个数字组成。
比如:
　　210×6=1260
　　8×473=3784
　　27×81=2187
　　都符合要求。
　　如果满足乘法交换律的算式算作同一种情况，那么,包含上边已列出的3种情况,一共有多少种满足要求的算式。
　　请填写该数字,通过浏览器提交答案,不要填写多余内容(例如:列出所有算式)。
""")

Magicformula = []
for i in range(1, 1000):
    for j in range(i+1, 1000):
        product = i * j
        if 1000 <= product <= 9999:
            list1 = [x for x in str(i)] + [x for x in str(j)]
            list2 = [x for x in str(product)]
            list1.sort()
            list2.sort()
            if list1 == list2 and len(set(list1)) == 4:
                print("{}×{}={}".format(i, j, product))
                Magicformula.append("{}×{}={}".format(i, j, product))
print(f"神奇算式共有 {len(Magicformula)} 个。")
