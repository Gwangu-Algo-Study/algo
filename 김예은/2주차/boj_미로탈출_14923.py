from collections import deque

N, M = map(int,input().split())
Hx, Hy = map(int,input().split())
Ex, Ey = map(int,input().split())
maps = [list(map(int, input().split()) for _ in range(N))]


# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 방문기록
visited = [[0]*M for _ in range(N)]
q = deque()

# 지팡이 사용


# 시작점 추가
q.append(Hx,Hy,0)
visited[Hx][Hy] = 1

while q:
    y, x, cost = q.popleft()
    if maps[y][x] =