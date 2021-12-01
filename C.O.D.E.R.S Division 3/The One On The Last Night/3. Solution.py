t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a = [int(i) for i in str(n)]
    a.sort()
    pdt=1
    while(k>0):
        if(a[0]==9):
            break
        a[0] = a[0]+1 
        a.sort()
        k-=1
    for i in range(len(a)):
        pdt = pdt * a[i]
    print(pdt)
