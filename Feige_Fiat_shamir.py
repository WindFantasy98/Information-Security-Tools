# --------------------------------------

# 模
n=33
# k=2
# 秘密密钥
mimi=[5,2,8,4]
# 公开密钥
openm=[4,25,16,31]

# --------------------------------------

# 1. 随机数，需要自己设置！
randnum=7

outp1=randnum**2%n
print('发送数：')
print(outp1)


# 2. 随机串，需要自己设置！
randlist=[1,1,0,0]

outp2=randnum
for i in range(len(randlist)):
    t=mimi[i]**randlist[i]
    outp2=outp2*t
outp2=outp2%n
print('再次发送数：')
print(outp2)


# 3.验证
# 刚收到的数**2 * 公钥按位方 mod n == 第一次发送的数

