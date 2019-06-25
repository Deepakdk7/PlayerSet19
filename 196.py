ax=int(input())
a=input().split()
b=[]
c=[]
d=[]
e=0
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    for j in range(0,len(a)):
        if i==a[j]:
            c.append(a.count(i))
            c.append(i)
            d.append(a.count(i))
e=min(d)
for i in range(0,len(c)):
    if c[i]==e:
        print(c[i+1])
