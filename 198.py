ax=int(input())
a=list(map(int,input().split()))
a.sort()
print(a.index(a[len(a)-1])-a.index(a[0]))
