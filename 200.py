ax=list(input())
a=[]
for i in ax:
    if i not in a:
        a.append(i)
print(*a,sep='')
