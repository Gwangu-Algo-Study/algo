import sys
dct=list(map(int,sys.stdin.readline().split()))
result=dct[0]-dct[1]
for i in range(1,len(dct)-1):
    # 조건입니다. 순차적으로 변속하는게 아니거나, 단수를 낮추다가 올리는 경우를 판별해서 mixed를 출력합니다.
    if (result != 1 and result !=-1) or (result !=dct[i]-dct[i+1]):
        result=100
        print('mixed ')
        break
    else:
        result=dct[i]-dct[i+1]
if result==-1:
    print('ascending')
elif result==1:
    print('descending')