from collections import deque
n, m = map(int, input().split())
prints = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 그림 개수와, 가장 넓은 그림의 넓이
def bfs(x,y):
    area = 1
    q = deque()
    q.append((x,y))
    prints[x][y] = 0
    # 함수 내부에서는 숫자값을 보내주고, 외부에서는 숫자가 있으면 카운트 1 하는 방식으로 세기
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if prints[nx][ny] == 1:
                prints[nx][ny] = 0
                area += 1
                q.append((nx,ny))
    return area

cnt = 0
areas = 0
for i in range(n):
    for j in range(m):
        if prints[i][j]:
            paintings = bfs(i,j)
            if paintings:
                cnt += 1
                areas = max(areas, paintings)


print(cnt)
print(areas)