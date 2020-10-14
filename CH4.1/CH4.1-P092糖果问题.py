# 4.1.4：拓展练习：糖果
"""
原题如下：
    假设有20颗糖果，两人轮流取糖果，每次可以取1至2颗，拿到最后一颗糖果的人获胜；你可以自由选择先取还是后取糖果。
    请设计一个必赢的算法并用流程图表示。


分析（假设其中一个人是我，且我想赢）：
    如果拿到最后一颗即20颗糖果就赢，且每次只能拿1-2颗，那只需要拿到17颗糖果就可以了。
    当我拿到17，此时对方再拿1颗或2颗的任何一种都到不了20颗，反而只需要等对方拿完后我再拿一次就到20了，比如对方拿2，就到19颗我再拿个1颗就到20，
对方拿1，我拿2就到20。
    怎样才能拿到26颗呢，想一想：
    首先我们观察一下每次拿糖果的数：1、2，这二个数能不能两两组合成一个固定的数，我们发现，1+2=3，所以这个固定的组合数就是3。
    由此得方案：
    目标数 20 减去“最多拿 2 颗”中的2，再减1得17
    如果 17 能被组合数 3 整除，则只需要对方先出，然后我每次拿一个和对方相加和为3的数即可，最后我一定能数到20；
    但很明显此处的17不能被组合数 3 整除，所以：
    走第一次时一定要掌握主动权，将 17 转化为可以被 3 整除的数，即 17 减去我第一次拿走的糖果数后需要能被 3 整除。
    故我第一次，且必须拿 2 。因为 17 - 2 = 15,  得到的 15 能被 3 整除(17 % 3 = 2)
    接下来只需要等对方拿糖果，（随便拿1-2中哪个数量糖果），我方只需要拿一个和对方数字相加为 3 的数量即可胜利！
    (15/3=5 。即五轮后我就能拿到20)
答案：
    我先拿，拿2颗；接下来我只需要拿一个和对方相加为 3 的数量即可我赢

"""


def myfunc(n, stepper):
    """
    :参数 n: 目标数
    :参数 stepper: 步进范围（可以走几步的最大值）
    :返回值: （flag,first_num,total_stepper）
            第一个出还是第二个出：flag=1,第一个出；flag = 0第二个出
                如果第一个出：第一次出多少 first_num
                如果第二个出：出的数总和为多少 total_stepper
    """
    total_stepper = stepper + 1  # 组合数
    if n % total_stepper == 0:  # 能整除的情况
        print("目标数：{}，步进范围：{}，组合数：{}".format(n, stepper, total_stepper))
        flag = False   # 对方先出
        return flag, 0, total_stepper
    else:
        v_num = n - stepper - 1  # 拿到v_num就一定能数到目标数
        if v_num % total_stepper == 0:  # v_num能被组合数整除的情况
            flag = False  # 对方先出
            print("目标数：{}， 步进范围：{}， 组合数：{}, 是否第一个出：{}".format(n, stepper, total_stepper, flag))
            return flag, 0, total_stepper
        else:
            flag = True  # 我方先出
            first_num = v_num % total_stepper  # 我第一次数的数，这个数将v_num钝化为可以被组合数整除的数
            printstring = "目标数：{}， 步进范围：{}， 组合数：{}, 是否第一个出：{}, 出多少：{}"
            print(printstring.format(n, stepper, total_stepper, flag, first_num))
            return flag, first_num, total_stepper


if __name__ == "__main__":
    print(myfunc(20, 2))
    print(myfunc(32, 3))
    print(myfunc(60, 7))
