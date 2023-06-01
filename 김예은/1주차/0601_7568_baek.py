N =  int(input())
manlist = []
order = [0]*N
for _  in range(N):
    # 키와 몸무게 입력 받기
    t, w = map(int, input().split())
    # 리스트에 튜플 값으로 저장
    manlist.append((t,w))

#몸무게가 나보다 큰지 확인, 근데 걔가 나보다 키도 크면 1명인것임.

for i in range(len(manlist)):
    k = 1
    for j in range(len(manlist)):
        # 나보다 무겁고
        if manlist[i][0] < manlist[j][0]:
            # 키큰사람이 있다면
            if manlist[i][1] < manlist[j][1]:
                # 등수 밀려남
                k += 1
    #  등수 리스트에 저장
    order[i] = k

print(*order)

