def gcd(a,b):
    if a<b:
        t=b
        b=a
        a=t
    if b==0:
        return a
    else:
        return gcd(b,a%b)


if __name__ == "__main__":
    a=24
    b=32
    print(gcd(a,b))
