from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy, maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited[n - 1][m - 1]


def solution(maps):
    i, j = 0, 0

    answer = bfs(i, j, maps)
    if answer == 0:
        answer = -1
    return answer