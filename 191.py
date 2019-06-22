ax=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))[::-1]
if a==b:
    print('yes')
else:
    print('no')
