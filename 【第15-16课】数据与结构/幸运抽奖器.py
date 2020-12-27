import csv
import random


# 定义个抽奖类，功能有输入抽奖级别和个数，打印出每个级别的抽奖员工号码
class ChouJiang:
    # 定义scv文件路径
    def __init__(self, filepath):
        self.emp_file = filepath

    def creat_num(self):
        emp_list = []
        with open(self.emp_file, "r", encoding='UTF-8') as f:
            emp_f = csv.reader(f)
            for emp in emp_f:
                emp_list.append(emp[0])
        print('共有 {} 人参与抽奖'.format(len(emp_list)))

        # 进行抽奖开始
        luckier_dict = {}

        while True:
            str_level = input('抽奖层次，请输入：')
            if str_level == '0':
                break
            if str_level in luckier_dict.keys():
                print("当前奖项已有 {} 人")
                _luckier = luckier_dict[str_level]
            else:
                _luckier = []
            str_level_dict_key = input('请输入当前获奖 {} 对应的奖品个数：'.format(str_level))
            int_level_dict_key = int(str_level_dict_key)
            winners = []
            print('抽奖层次 {} 的获奖人员有：'.format(str_level))
            # 产生当前抽奖层次i对应的抽奖个数
            for j in range(int_level_dict_key):
                # 利用random模块中的choice函数从列表中随机产生一个
                winner = random.choice(emp_list)
                winners.append(winner)
                emp_list.remove(winner)
                print("  ", winner)
            luckier_dict[str_level] = _luckier + winners
        return luckier_dict


def save_txt(_luckier, _file='luckier.txt'):
    with open(_file, "w") as f:
        for key, value in _luckier.items():
            f.write('[{}]\n'.format(key))
            for item in value:
                f.write('{}\n'.format(item))


if __name__ == '__main__':
    peoples = ChouJiang('luckier.csv')
    luckier = peoples.creat_num()
    save_txt(luckier)
