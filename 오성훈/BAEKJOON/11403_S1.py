N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = [[0] * N for _ in range(N)]
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