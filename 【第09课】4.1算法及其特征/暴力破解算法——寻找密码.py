import time

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def find_pwd(deep, parent):
    if deep == 1:
        if parent == password:
            print("你的密码是：", parent)
            return True
        else:
            return False
    else:
        for j in range(len(char)):
            if find_pwd(deep - 1, parent + char[j]):
                return True
    return False


def get_char(char_type):
    char_set = []
    if char_type == 1:
        char_set = number
    elif char_type == 2:
        char_set = ALPHABET
    elif char_type == 3:
        char_set = alphabet
    elif char_type == 4:
        char_set = number + ALPHABET
    elif char_type == 5:
        char_set = number + alphabet
    elif char_type == 6:
        char_set = ALPHABET + alphabet
    elif char_type == 7:
        char_set = number + ALPHABET + alphabet
    return char_set


set_type = {1: '数字',
            2: '大写字母',
            3: '小写字母',
            4: '数字+大写字母',
            5: '数字+小写字母',
            6: '字母(区分大小写)',
            7: '数字+字母(区分大小写)'}
password = "25321"
for char_set_type in [1, 4, 7]:
    char = get_char(char_set_type)
    t1 = time.time()
    for psw_length  in range(1, 18):
        pwd = ""
        flag = False
        for i in range(len(char)):
            if find_pwd(psw_length, pwd + char[i]):
                flag = True
                break
        if flag:
            break
    print("密码类型:{} \n破解用时：{:.2f}秒".format(set_type[char_set_type], time.time() - t1))
