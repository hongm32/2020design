while True:
    string = input("输入你要查询编码的字符(串)：")
    if string.lower() in ['quit', 'exit']:
        break

    for s in string:
        print("“{}”的编码：".format(s))
        string_1 = string_2 = string_3 = string_4 = string_5 = ""
        s_gbk = s.encode('gbk')
        s_utf = s.encode()
        s_unicode = ord(s)
        if s_unicode > 255:
            for i in s_gbk:
                string_1 += str(i - 160)
                string_2 += hex(i - 128).replace("0x", "").upper()
                string_3 += hex(i).replace("0x", "").upper()
            string_4 += hex(ord(s)).replace("0x", "").upper()
            print("  区位码是{}D".format(string_1))
            
            print("  国标码是{}H".format(string_2))
            print("  机内码是{}H".format(string_3))
            print(" Unicode是{}H".format(string_4))
        else:
            string_5 = ord(s)
            print("   ASCII是{}".format(string_5))
        
        # UTF-8编码规则
        #    1)对于单字节的符号，字节的第一位设为0，后面7位为这个符号的unicode码。因此对于英语字母，UTF-8编码和ASCII码是相同的。
        #    2)对于n字节的符号（n>1），第一个字节的前n位都设为1，第n+1位设为0，后面字节的前两位一律设为10。
        #      剩下的没有提及的二进制位，全部为这个符号的unicode码。
        # Unicode符号范围      | UTF8编码方式
        # 0000 0000-0000 007F | 0xxxxxxx
        # 0000 0080-0000 07FF | 110xxxxx 10xxxxxx
        # 0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
        # 0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
        str_unicode = ord(s)
        s_bin = "0" * 8 + bin(str_unicode)[2:]
        str_utf = None
        if str_unicode <= 0x7F:
            str_utf = s_bin[-8:]
        elif str_unicode <= 0x7FF:
            str_utf = "110" + s_bin[-13:-6] + "10" + s_bin[-6:]
        elif str_unicode <= 0xFFFF:
            str_utf = "1110" + s_bin[-16:-12] + "10" + s_bin[-12:-6] + "10" + s_bin[-6:]
        elif str_unicode <= 0x10FFFF:
            str_utf = "11110" + s_bin[-21:-18] + "10" + s_bin[-18:-12] + "10" + s_bin[-12:-6] + "10" + s_bin[-6:]
        str_utf_code = hex(int(str_utf, 2)).replace("0x", "").upper()
        print("   UTF-8是{}H".format(str_utf_code))
        # 可以用以下方法string.encode()：
        # print("   UTF-8是{}H".format(str(s.encode())[4:-1].replace("\\x", "").upper()))
