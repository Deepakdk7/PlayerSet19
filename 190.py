ax=list(map(int,input().split()))
ax.sort(reverse=True)
if ((ax[1]**2)+(ax[2]**2))==(ax[0]**2):
    print('yes')
else:
    print('no')
