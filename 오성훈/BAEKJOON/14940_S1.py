import sys
from collections import deque

# 단순 bfs와 거의 같다.
def bfs(goal_x, goal_y):
    que = deque()
    que.append([goal_y, goal_x, 1])
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    while que:
        y, x, distance = que.popleft()
        for i in range(4):
            if y+di[i] >= 0 and y+di[i] < n and x+dj[i] >= 0 and x+dj[i] < m and visited[y+di[i]][x+dj[i]] == 0 and arr[y+di[i]][x+dj[i]] == 1:
                visited[y+di[i]][x+dj[i]] = 1
                arr[y+di[i]][x+dj[i]] = distance
                que.append([y+di[i], x+dj[i], distance+1])
        

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(m)]
goal_x = -1
goal_y = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            goal_y = i
            goal_x = j
            break
    if goal_x != -1:
        break
# 초기 조건 설정
visited[goal_y][goal_x] = 1
arr[goal_y][goal_x] = 0
bfs(goal_x, goal_y)

# 못 가는 곳은 -1
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and arr[i][j] == 1:
            arr[i][j] = -1
    
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()