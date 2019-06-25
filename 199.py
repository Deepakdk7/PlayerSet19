ax=list(input())
if len(ax)==1 or len(ax)==2:
    print('yes')
else:
    i=1
    j=len(ax)-1
    for n in range(1,len(ax)):
        if ax[i]==ax[j]:
            print('yes')
            break
        else:
            print('no')
            break
