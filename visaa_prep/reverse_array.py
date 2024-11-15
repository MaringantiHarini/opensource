def array(n):
    for i in range(0,n):
        a=list(map(int,input().split()))
        return " ".join(map(str,a[::-1]))
n=int(input())
print(array(n))
