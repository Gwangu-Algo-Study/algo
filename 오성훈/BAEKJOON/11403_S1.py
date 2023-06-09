N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = [[0] * N for _ in range(N)]

# 입력받은 arr에서 플로이드-워셜 이용
# 경로의 유무를 묻고 있으므로 가중치는 제외하고 길이 있는지만 판단
for i in range(N):
    for j in range(0, i):
        if arr[j][i] == 1:
            for k in range(N):
                arr[j][k] = max(arr[i][k], arr[j][k])
    for j in range(i+1, N):
        if arr[j][i] == 1:
            for k in range(N):
                arr[j][k] = max(arr[j][k], arr[i][k])
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()