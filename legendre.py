def legendre(a,p):
    t=(p-1)/2
    b=a**t%p
    if b==0:
        print("a被p整除")
    elif b==1:
        print("a是p的二次剩余")
    elif b==p-1:
        print("a是p的非二次剩余")
    else:
        print(b)


if __name__ == "__main__":

# --------------------------------------

    a=6
    p=11
    
# --------------------------------------

    legendre(a,p)