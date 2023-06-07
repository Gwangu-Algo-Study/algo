import sys
from collections import deque
n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
# 일반 사람
que = deque()
visited = [[0] * n for _ in range(n)]
cnt_normal = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt_normal += 1
            que.append([i, j])
            visited[i][j] = 1
        while que:
            y, x = que.popleft()
            for k in range(4):
                if y+di[k] >= 0 and y+di[k] < n and x+dj[k] >= 0 and x+dj[k] < n and visited[y+di[k]][x+dj[k]] == 0 and arr[y][x] == arr[y+di[k]][x+dj[k]]:
                    que.append([y+di[k], x+dj[k]])
                    visited[y+di[k]][x+dj[k]] = 1

# 적록색약인사람
visited = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt += 1
            que.append([i, j])
            visited[i][j] = 1
        while que:
            y, x = que.popleft()
            for k in range(4):
                if y+di[k] >= 0 and y+di[k] < n and x+dj[k] >= 0 and x+dj[k] < n and visited[y+di[k]][x+dj[k]] == 0:
                    if ((arr[y][x] == 'R' or arr[y][x] == 'G') and (arr[y+di[k]][x+dj[k]] == 'R' or arr[y+di[k]][x+dj[k]] == 'G')) or (arr[y][x] == arr[y+di[k]][x+dj[k]]):
                        que.append([y+di[k], x+dj[k]])
                        visited[y+di[k]][x+dj[k]] = 1

print(cnt_normal, cnt)