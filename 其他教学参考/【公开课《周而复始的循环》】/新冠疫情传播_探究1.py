print("""某病毒感染像模人体后，会进行自我复制，
默认速度参数为2，即一个同期由1个变为2个，
如免疫力强，病毒则以2以下的速度复制；如免疫力弱，病毒以2以上的速度复制。
探究：
某人感染某病毒，初始病毒数量为100，探究不同复制速度(免疫力不同)下的感染情况。
小于10 可认为治愈；10~1000为潜伏期；大于1000为症状期。
""")

rate = float(input("请输入病毒复制的速度参数："))
total_sum = 100
for i in range(1, 11):
    total_sum *= rate
if total_sum < 10:
    print("到第10周期时，病毒数变为{}，病人已痊愈。".format(int(total_sum)))
elif total_sum < 1000:
    print("到第10周期时，病毒数变为{}，病人处于潜伏期。".format(int(total_sum)))
else:
    print("到第10周期时，病毒数变为{}，病人处于症状期。".format(int(total_sum)))
input("运行完毕，按回车键退出...")
