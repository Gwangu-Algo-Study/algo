import sys
w,n=map(int,sys.stdin.readline().split())
rock=[]
result=0
for i in range(n):
    rock.append(list(map(int,sys.stdin.readline().split())))
    # 귀중속 리스트를 만듭니다
rock.sort(key=lambda x:-x[1])
# 최대 값으로 하기 위해 비싼것부터 넣어야되니 단가를 기준으로 정렬을 합니다.
for i in range(n):
    if w>rock[i][0]:
        result+=rock[i][0]*rock[i][1]
        # 귀중속을 챙기고 금액을 기록합니다
    else:
        result+=rock[i][1]*w
        # 가방에 넣을수 있는 무게보다 해당 차례의 귀중속의 무게가 더 크다면 이거 넣고 다음꺼는 넣을 필요가 없으니 남은 가방 무게만큼 금액을 기록하고 끝냅니다.
        break
    w-=rock[i][0]
    # 가방에 넣을 수 있는 무게를 최신화합니다.
print(result)