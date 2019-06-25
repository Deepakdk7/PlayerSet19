x,y,z=list(map(int,input().split()))
if (x+y)>z and (x+z)>y and (y+z)>x and a!=b and a!=c and a!=b!=c:
    print('yes')
else:
    print('no')
