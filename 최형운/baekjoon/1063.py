import sys
input=sys.stdin.readline
move={'R':[1,0],"L":[-1,0],'B':[0,-1],'T':[0,1],'RT':[1,1],"L":[-1,1],'RB':[1,-1],'LB':[-1,-1]}
k,dol,n=input().split()
kPosi=[ord(k[0]) - 64,int(k[1])]
dolPosi=[ord(k[0]) - 64,int(dol[1])]
for _ in range(int(n)):
    moving=input()
    a=move[moving[:-1]]
    if 1<=kPosi[0]+a[0]<=8 and 1<=kPosi[1]+a[1]<=8:
        kPosi = [kPosi[0]+a[0], kPosi[1]+a[1]]
    if 1<=dolPosi[0]+a[0]<=8 and 1<=dolPosi[1]+a[1]<=8:
        dolPosi = [dolPosi[0]+a[0], dolPosi[1]+a[1]]

print(chr(kPosi[0] + 64)+str(kPosi[1]))
print(chr(dolPosi[0] + 64)+str(dolPosi[1]))
