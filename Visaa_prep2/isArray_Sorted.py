n=int(input())
arr=list(map(int,input().split())) 
sort="true"
for i in range(0,len(arr)-1):
    if arr[i]>arr[i+1]:
        sort='false'
        break
print(sort)
