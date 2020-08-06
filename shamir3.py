arr = [0, 1, ]

def Exclude_GCD(a, b, arr):  # 扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    ans = Exclude_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return ans

def ModReverse(a, n):  # ax=1(mod n) 求a模n的乘法逆x
    arr = [0, 1, ]
    gcd = Exclude_GCD(a, n, arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1

# --------------------------------------

# p
p=11
# 甲密钥e1
e1=3
# 乙密钥e2
e2=9
# 密文
M=4

# --------------------------------------


temp=p-1
d1=ModReverse(e1,temp)
d2=ModReverse(e2,temp)
print('e1关于模p-1的逆元是')
print(d1)
print('e2关于模p-1的逆元是')
print(d2)

C1=M**e1%p
print('C1=M**e1 mod p')
print(C1)

C2=C1**e2%p
print('C2=')
print(C2)

C3=C2**d1%p
print('C3=')
print(C3)


M2=C3**d2%p
print('M=')
print(M2)
