di = [-1,1,0,0]
dj = [0,0,-1,1]


def bfs(si,sj,N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((si,sj))
    visited[si][sj] = 1

    while True:
        i, j = q.pop(0)
        # 만약 끝지점이면
        if i == N-1 and j == N-1:
            return 1

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and blocks[ni][nj] != 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
                i, j = ni, nj
            else:
                if q:
                    i, j = q.pop()
                # 스택이 비어있으면 반복을 종료.
                else:
                    break

        return 0
N = int(input())
blocks = [list(map(int, input())) for _ in range(N)]
si = sj = 0
print(blocks)
print(bfs(si,sj,N))
