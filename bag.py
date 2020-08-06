def bag():
    # 求解秘密密钥
    #---------------------------------- 
    # 模
    m=
    n=
    # 公开密钥向量
    arr=[]

    #---------------------------------- 

    l=len(arr)
    ans=[]
    for x in arr:
        k=1
        while True:
            if k*n%m== x:
                ans.append(k)
                break
            k+=1
    print("秘密密钥")
    print(ans)
    return ans


def solve(mimi,num):
    # 根据秘密密钥 和 求模后密文 计算得到加密明文，也可用于递增序列分解
    l = len(mimi)-1
    ls=[]
    ans=[]
    for i in range(l+1):
        ans.append(0)
    while l>=0:
        if num>=mimi[l]:
            num-=mimi[l]
            ans[l]=1
        elif num<=0:
            break
        l-=1
    print("加密明文")
    print(ans)


if __name__ == "__main__":
    mimi=bag()
    # 这里需要手动计算得到密文
    # mimi=
    miwen=
    solve(mimi,miwen)
