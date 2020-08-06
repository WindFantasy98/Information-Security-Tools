def isprime(n):  # 判断素数
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

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

# 公开密钥
n=3337
e=79

# 明文，小于3位
M=232

# --------------------------------------

ls=[]
i=2
while i<n:
    if isprime(i):
        ls.append(i)
    i+=1

p=-1
q=-1
for num in ls:
    if n%num==0:
        if isprime(n/num):
            p=num
            q=int(n/num)

print('n的质因数分解结果')
print(p)
print(q)

tmod=(p-1)*(q-1)
print('中间结果 模为')
print(tmod)

d=ModReverse(e,tmod)
print('d= e-1 mod tmod的结果是')
print(d)

c=M**e%n
print('加密结果：')
print(c)

cc=c**d%n
print('解密结果')
print(cc)

