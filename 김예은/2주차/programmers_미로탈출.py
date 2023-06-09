from collections import deque


def bfs(s, e, maps):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n, m = len(maps), len(maps[0])

    # 방문 기록
    visited = [[0] * m for _ in range(n)]
    q = deque()
    flag = 0
    for i in range(n):
        for j in range(m):
            #만약 시작점이라면
            if maps[i][j] == s:
                #스타트 노드에 추가
                q.append((i, j, 0))
                #방문처리
                visited[i][j] = 1
                flag = 1
                break
        if flag:
            break

    while q:
        y, x, cost = q.popleft()
        # 끝점이라면, 경로 return
        if maps[y][x] == e:
            return cost
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'X':
                if not visited[ny][nx]:
                    q.append((ny, nx, cost + 1))
                    visited[ny][nx] = 1
    return -1


def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)
    if path1 != -1 and path2 != -1:
        return path1 + path2
    return -1
