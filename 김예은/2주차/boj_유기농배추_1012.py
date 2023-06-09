from collections import deque

T = int(input())

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    maps[x][y] = 0


    while q:
        x,y =  q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                continue
            if maps[nx][ny]:
                # 탐색한 배추들을 모두 0으로 만든다.
                maps[nx][ny] = 0
                q.append((nx,ny))
    return True


for _ in range(T):
    M, N, K = map(int, input().split())
    maps = [[0]* N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        maps[x][y] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            # 배추가 있다면 bfs로 인접 배추를 탐색한다.
            if maps[i][j]:
                cnt += bfs(i, j)
    print(cnt)
