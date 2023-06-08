from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # 방문 배열 생성
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0,0))

    # 우하좌상 방향으로 배열 생성
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    visited[0][0] = True

    while q :
        x, y = q.popleft()
        # 4 방향을 돌면서 연산
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 만약 nx와 ny가 접근 가능한 인덱스이며 maps에서 벽이 아닌 위치의 경우
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                # 그리고 아직 방문하지 않은 경우
                if not visited[ny][nx] :
                    visited[ny][nx] = True
                    q.append((nx, ny))
                    # 지금까지의 거리 +1 하여 저장
                    maps[ny][nx] = maps[y][x]+1

    if maps[n-1][m-1] == 1:
        return -1
    else :
        return maps[n-1][m-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))