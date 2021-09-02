# Dayday_up.py
"""
问题：工作日的努力
工作日模式要努力到什么水平，才能与同学古怪的努力1%一样？
-A君：一年365天，每天进步1%，不停歇
-B君：一年365天，每周工作5天休息2天，休息日下降1%，要多努力呢？
"""
A = pow(1.01, 365)


def day_day_up(df):
    day_up = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            day_up = day_up * (1 - 0.01)
        else:
            day_up = day_up * (1 + df)
    return day_up


day_factor = 0.01
while day_day_up(day_factor) < A:
    day_factor += 0.00001
print("工作日的努力参数是：{:.5f}，即{:.2f}%".format(day_factor, day_factor * 100))
print("若按{:.2f}%天天努力则为原来的{:.1f}倍".format(day_factor * 100, pow(1 + day_factor, 365)))

input("运行完毕，请按回车键退出...")
