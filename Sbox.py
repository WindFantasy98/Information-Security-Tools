s1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

s2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

s3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

s4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

s5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

s6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

s7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

s8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
def string2Binary(str):
    le = len(str)
    dest = [0] * le * 4
    i = 0
    for c in str:
        i += 4
        j = 0
        s = hex2bin(c)
        l = len(s)
        for d in s:
            dest[i - l + j] = int(d)
            j += 1
    return dest
# dec2hex
# 十进制 to 八进制: oct()
# 十进制 to 十六进制: hex()
def dec2hex(string_num):
    num = int(string_num)
    if num == 0:
        return '0'
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])
def press(source):
    global s_box
    ret = [0] * 32
    temp = [([0] * 6) for i in range(8)]
    s = [s1, s2, s3, s4, s5, s6, s7, s8]
    st = []
    for i in range(8):
        for j in range(6):
            temp[i][j] = source[i * 6 + j]
    for i in range(8):
        # (16)
        x = temp[i][0] * 2 + temp[i][5]
        # (2345)
        y = temp[i][1] * 8 + temp[i][2] * 4 + temp[i][3] * 2 + temp[i][4]
        val = s[i][x][y]
        ch = dec2hex(str(val))
        # System.out.println("x=" + x + ",y=" + y + "-->" + ch);
        # String ch = Integer.toBinaryString(val);
        st.append(ch)

    # System.out.println(str.toString());
    ret = string2Binary(st)

    print("可能是第一次s盒")
    print(ret)
    for i in range(32):
        if(i%8 == 0 and i/8>=1):
            print()
        if(i%4 == 0):
            print(end='  ')
        print(ret[i],end='')
    s_box =ret
    # printArr(ret);
    # 置换P
    ret = dataP(ret)
    return ret
def dataP(source):
    dest = [0] * 32
    temp = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31,
            10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    le = len(source)
    for i in range(le):
        dest[i] = source[temp[i] - 1]
    return dest
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]
# 十六进制 to 十进制
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))
# dec2bin
# 十进制 to 二进制: bin()
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))
'输入样例100100 000000 000010 101110 101000 001010 100001 010010学号扩展后的结果'
# 000000 010000 000100 000001 000000 010000 000100 000010
# 我的学号扩展201756301130
# 0000 0000 0000 0000 0010 0000 0001 0111 0101 0110 0011 0000

plainText = input("需要转化的二进制序列")
plainText = plainText.replace(' ', '')  # 去除明文中多余空格
a= list(plainText)
t = []
for i in a:
    t.append(int(i))
print(t)

press(t)