import sys
sys.setrecursionlimit(10**6)
T = int(input())
for _ in range(T):
    # 상우하좌 순서로 탐색
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    M, N, K = map(int, input().split())
    # 미리 0으로 다 채워주기
    land = [[0]*M for _ in range(N)]
    result = 0
    # 배추가 있는 곳에 1로 채워줌
    for i in range(K):
        x, y = map(int, input().split())
        land[y][x] = 1

    # land[i][j]의 사방을 탐색해서 배추가 있으면(1일 경우) 재귀로 한번 더 실행
    def check_land(i, j):
        if land[i][j]:
            # 다시 탐색이 되지 않게 하기 위해 0으로 바꿔줌
            land[i][j] = 0
            for k in range(4):
                ci = i + di[k]
                cj = j + dj[k]
                if (0 <= ci < N) and (0 <= cj < M) and land[ci][cj] == 1:
                    check_land(ci, cj)


    # land 전체 탐색
    for i in range(N):
        for j in range(M):
            # 1일 경우 check_land 함수 실행
            if land[i][j] == 1:
                check_land(i,j)
                result += 1
    print(result)

