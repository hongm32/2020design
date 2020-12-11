def insert0(s):  # 摩尔斯符号转为二进制灯语
    if len(s) > 0:
        t = s[0]
        for i in range(1, len(s)):
            t += '0' + s[i]
        t = t.replace('.', '1')
        t = t.replace('-', '111')
        return t


def encode():
    words = input("请输入明文(由英文数字空格组成的字符串):").strip().upper()
    m = ''
    d = ''
    for letter in words:
        if letter == ' ':
            if m[-1] != '/':
                m = m.strip() + '/'
            if d[-7:] == '0' * 7:
                pass
            elif d[-3:] == '0' * 3:
                d += '0' * 4
            else:
                d += '0' * 7
        else:
            m += dict1[letter] + ' '
            d += insert0(dict1[letter]) + '0' * 3
    m = m.strip() + '/'
    if d[-3:] == '0' * 3:
        d += '0' * 4
    else:
        d += '0' * 7
    print('[摩尔斯码为]' + m)
    print('[灯  语  为]' + d)


def decode():
    codes = input("请输入灯语(由明(1)暗(0)组成的字符串):").strip().split("0" * 7)
    u = ''
    m = ''
    for i in codes:
        if i != '':
            t = i.split('0' * 3)
            for j in t:
                if j != '':
                    s = j.split('0')
                    v = ''
                    for k in s:
                        if k != '':
                            k = k.replace('111', '-')
                            k = k.replace('1', '.')
                            v = v + k
                    m += dict2[v]
                    u += v
                    u += ' '
            u = u[:-1]
            u += '/'
            m += ' '
    m = m[:-1]
    print('[摩尔斯码为]' + u)
    print('[明  文  为]' + m)


# dict of words2morse
dict1 = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
         'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
# dict of morse2words
dict2 = dict(zip(dict1.values(), dict1.keys()))
while True:
    print('编码(明文转为摩尔斯码、灯语)  0\n解码(灯语转为摩尔斯码、明文)  1')
    choice = input("请输入您的选择[0/1/其他]:     ")
    if choice == '0':
        encode()
    elif choice == '1':
        decode()
    else:
        break
