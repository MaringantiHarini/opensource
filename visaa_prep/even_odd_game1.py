n=int(input())
s=0
while(n):
    rem=n%10
    s+=rem
    n//=10
    
if s%2==0:
    print("Vignesh")
else:
    print("Charan")
