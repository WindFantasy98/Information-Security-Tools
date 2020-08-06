#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np 

#扩展欧几里得算法求最大公约数gcd
def EX_GCD(a,b,arr): #扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = EX_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return g

#求乘法逆元
def ModReverse(a,n): #ax=1(mod n) 求a模n的乘法逆x
    arr = [0,1,]
    gcd = EX_GCD(a,n,arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1


if __name__ == "__main__":
# --------------------------------------

    n = 29 #模26
    list_A1 = [] 
    #目标矩阵A1
    A1 = np.array([[1,6],[5,3]])

# --------------------------------------

    #1.求伴随矩阵A2
    #np.linalg.inv(A1)目标矩阵的逆
    #np.linalg.det(A1)目标矩阵的行列式
    #伴随矩阵 = 行列式 * 矩阵的逆= np.linalg.inv(A1) * np.linalg.det(A1)
    for i in range((np.linalg.inv(A1) * np.linalg.det(A1)).shape[0]):
        for j in range((np.linalg.inv(A1) * np.linalg.det(A1)).shape[1]):
            list_A1.append(round((np.linalg.inv(A1) * np.linalg.det(A1))[i][j]))#round(x,n)n是表示保留几位小数，不写n默认是整数即n=0。

    A2 = np.array([list_A1],dtype=int)#伴随矩阵
    A2 = A2.reshape(A1.shape[0],A1.shape[1])#重塑矩阵,行列信息和A1相同。

    #2.求((1/行列式)%26) A3。
    #注意当行列式过大之后 （1/行列式）再进行模运算的时候会造成较大精度误差。通过除法改乘法来减小精度误差（1/行列式）% 26 =（1*行列式的乘法逆元）%26。
    A3 = ModReverse(round(np.linalg.det(A1)),n)
  
    #3.求逆矩阵A4
    A4 = (A3 * A2) % n

    print("得到目标矩阵A1的逆：\n %s" % A4)


# In[ ]:




