ax=int(input())
a=list(map(int,input().split()))
c=n=0
while n in a:
        a.remove(n)
        c=c+1
for i in range(0,c):
    a.append(0)
print(*a)
