import math
n = int(input())
for i in range(n):
    n1,x,k = map(int,input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = 0
    for i in range(n1):
        if(abs(a[i]-b[i])<=k):
            c+=1
    if(c>=x):
        print("YES")
    else:
        print("NO")
