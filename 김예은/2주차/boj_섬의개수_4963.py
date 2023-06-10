from collections import deque

#상하좌우,좌상좌하 우상우하
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy))
    maps[sx][sy] = 0

    while q:
        sx, sy = q.popleft()
        for d in range(8):
            nx, ny = sx+dx[d], sy+dy[d]
            if nx < 0 or nx > h-1 or ny < 0 or ny > w-1:
                continue
            if maps[nx][ny]:
            #탐색한 섬들을 모두 0으로 만든다.
                maps[nx][ny] = 0
                q.append((nx,ny))
    return True


while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        maps = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j]:
                cnt += bfs(i,j)

    print(cnt)