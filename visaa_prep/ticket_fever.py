n=int(input())
for i in range(0,n):
    m,k=map(int,input().split())
    if m>k:
        print(m-k)
    else:
        print(0)
