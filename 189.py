x,y,z=list(map(int,input().split()))
if (x+y)>z and (x+z)>y and (y+z)>x:
    print('yes')
else:
    print('no')
