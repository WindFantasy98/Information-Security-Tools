#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 2014/10/16  wrote by yangyongzhen
# QQ:534117529
# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]

# __author__ = 'YangYongZhen'

base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


# bin2dec
# 二进制 to 十进制: int(str,n=10)
def bin2dec(string_num):
    return str(int(string_num, 2))


# hex2dec
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


# hex2tobin
# 十六进制 to 二进制: bin(int(str,16))
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))


# bin2hex
# 二进制 to 十六进制: hex(int(str,2))
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))


'''
/**
 * PBOC3DES 加密算法
 * @author Administrator
 *
 */
'''


class PBOC_DES():
    pass


'''
/** ***************************压缩替换S-Box************************************************* */
'''
subKey = [([0] * 48) for ll in range(16)]

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

ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

_ip = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
       38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
       36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
       34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
# 每次密钥循环左移位数
# LS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
LS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
'''
/**第一次s盒
 * IP初始置换
 * @param source
 * @return
 */
'''


def changeIP(source):#ip第一次变化
    global ip_1
    dest = [0] * 64
    global ip
    for i in range(64):
        dest[i] = source[ip[i] - 1]
    print("IP变化1")
    for k in range(64):
        if (k % 8 == 0 and int(k / 8) >= 1):
            print()
        # print(temp1[k], end=' ')
        print(dest[k], end=' ')
    print()
    ip_1 = dest
    return dest


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


'''
/**
 * IP-1逆置
 * @param source
 * @return
 */
'''


def changeInverseIP(source):
    dest = [0] * 64
    global _ip
    for i in range(64):
        dest[i] = source[_ip[i] - 1]
    return dest


'''
/**
 *
 * 获取轮子密钥(48bit)
 *
 * @param source
 *
 * @return
 *
 */
'''


def setKey(source):
    global subKey,subKey1,roleft
    # 装换4bit
    temp = string2Binary(source)
    # 6bit均分成两部分
    left = [0] * 28
    right = [0] * 28
    # 经过PC-1 4bit转换6bit
    temp1 = [0] * 56
    temp1 = keyPC_1(temp)
    # printArr(temp1);
    # 将经过转换的temp1均分成两部分
    for i in range(28):
        left[i] = temp1[i]
        right[i] = temp1[i + 28]
    # 经过16次循环左移，然后PC-2置换
    print()
    for i in range(16):
        left = keyLeftMove(left, LS[i])
        right = keyLeftMove(right, LS[i])
        for j in range(28):
            temp1[j] = left[j]
            temp1[j + 28] = right[j]
        subKey[i] = keyPC_2(temp1)
        subKey1 = subKey[0]
        roleft =temp1
        if(i==0):
            print("这是pc-1的左移一位的结果")
            for k in range(56):
                if (k % 8 == 0 and int(k / 8) >= 1):
                    print()
                # print(temp1[k], end=' ')
                print(roleft[k], end=' ')
            print()
            print("下面是K1")
            # print(subKey[0])
            # print(subKey1)
            for k in range(48):
                 if (k % 6 == 0 and int(k / 6) >= 1):
                      print()
                 print(subKey[0][k], end=' ')
            print()


'''
/**
 *
 * 6bit的密钥转换成48bit
 * @param source
 * @return
 *
 */
'''


def keyPC_2(source):
    dest = [0] * 48
    temp = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
    for i in range(48):
        dest[i] = source[temp[i] - 1]
    return dest


'''
/**
 *
 * 将密钥循环左移i
 * @param source 二进制密钥数
 * @param i 循环左移位数
 * @return
 *
 */
'''


def keyLeftMove(source, i):
    temp = 0
    global LS
    le = len(source)
    ls = LS[i]
    for k in range(ls):
        temp = source[0]
        for j in range(le - 1):
            source[j] = source[j + 1]
    source[le - 1] = temp
    return source


'''
/**
 *
 * 4bit的密钥转换成56bit
 * @param source
 * @return
 *
 */
'''


def keyPC_1(source):
    global pc_1
    dest = [0] * 56
    temp = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]
    print("这是PC-1,PPT中第一次变换")
    for i in range(56):
        dest[i] = source[temp[i] - 1]
        if (i % 8 == 0 and int(i/8)>=1):
            print()
        print(dest[i], end=' ')

    print()
    pc_1 = dest
    # for i in range(56):
    #     if (i % 8 == 0 and int(i / 8) >= 1):
    #         print()
    #     print(pc_1[i], end=' ')
    return dest


'''
/**
 * 两个等长的数组做异或
 * @param source1
 * @param source2
 * @return
 */
'''


def diffOr(source1, source2):
    le = len(source1)
    dest = [0] * le
    for i in range(le):
        dest[i] = source1[i] ^ source2[i]
    return dest


'''
/**
 *
 * DES加密--->对称密钥
 * D = Ln(32bit)+Rn(32bit)
 * 经过16轮置
 * @param D(16byte)明文
 * @param K(16byte)轮子密钥
 * @return (16byte)密文
 */
'''


def encryption(D, K):
    global ip_right32
    temp = [0] * 64;
    data = string2Binary(D)
    # 第一步初始置
    data = changeIP(data)
    left = [([0] * 32) for i in range(17)]
    right = [([0] * 32) for i in range(17)]
    for j in range(32):
        left[0][j] = data[j]
        right[0][j] = data[j + 32]
    setKey(K)  # sub key ok
    for i in range(1, 17):
        # 获取(48bit)的轮子密
        key = subKey[i - 1]
        if i==1:
            print("主函数中的key如下")
            print(key)
            subKey1 = key
        # L1 = R0
        left[i] = right[i - 1]
        if i==1:
            print("这是IP变化的后32位")
            print(left[i])
            ip_right32 = left[i]

        # R1 = L0 ^ f(R0,K1)
        if i ==1:
            fTemp = f(right[i - 1], key)  # 32bit
        if i==1:
            print("第一次P变换")
            print(fTemp)
        right[i] = diffOr(left[i - 1], fTemp)
        if i==1:
            print("第一次的R1")
            print(right[i])
    # 组合的时候，左右调换
    for i in range(32):
        temp[i] = right[16][i]
        temp[32 + i] = left[16][i]

    temp = changeInverseIP(temp)
    str = binary2ASC(intArr2Str(temp))
    return str


'''
/**
 * 8bit压缩2bit
 * @param source(48bit)
 * @return R(32bit) B=E(R)⊕K，将48 位的B 分成8 个分组，B=B1B2B3B4B5B6B7B8
 */
 '''


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
    s_box =ret
    # printArr(ret);
    # 置换P
    ret = dataP(ret)
    return ret


'''
/**
 * 置换P(32bit)
 * @param source
 * @return
 */
'''


def dataP(source):
    dest = [0] * 32
    temp = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31,
            10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    le = len(source)
    for i in range(le):
        dest[i] = source[temp[i] - 1]
    return dest


'''
/**
 * 2bit扩展8bit
 * @param source
 * @return
 */
'''


def expend(source):
    ret = [0] * 48
    temp = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12,
            13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22,
            23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    for i in range(48):
        ret[i] = source[temp[i] - 1]
    return ret


'''
/**
 * @param R(2bit)
 * @param K(48bit的轮子密
 * @return 32bit
 */
'''


def f(R, K):
    global ip_right_exband,xor_1
    dest = [0] * 32
    temp = [0] * 48
    # 先将输入32bit扩展8bit
    expendR = expend(R)  # 48bit
    print("IP后32位扩展")
    print(expendR)
    ip_right_exband = expendR
    # 与轮子密钥进行异或运
    temp = diffOr(expendR, K);
    print("与轮子密钥进行异或运")
    print(temp)
    xor_1 =temp
    # 压缩2bit
    dest = press(temp)
    # print("第一次s盒")
    # print(dest)
    return dest


'''
/**
 * 将int类型数组拼接成字符串
 * @param arr
 * @return
 */
'''


def intArr2Str(arr):
    sb = []
    le = len(arr)
    for i in range(le):
        sb.append(str(arr[i]))
    return ''.join(sb)


'''
/**
 * 将二进制字符串转换成十六进制字符
 * @param s
 * @return
 */
'''


def binary2ASC(s):
    st = ''
    ii = 0
    le = len(s)
    # 不够4bit左补0
    if le % 4 != 0:
        while ii < (4 - len % 4):
            s = "0" + s
    le = int(le / 4)
    for i in range(le):
        st += bin2hex(s[i * 4: i * 4 + 4])
    return st


if __name__ == "__main__":
    D = '0123456789abcdef'
    K = 'fedcba9876543210'
    print(encryption(D, K))
    # print(subKey1)
    # print(roleft)
    # print(pc_1)
    # print(ip_1)
    # print(ip_right32)
    # print(ip_right_exband)
    # print(xor_1)

