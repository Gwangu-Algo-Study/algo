from collections import deque
N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]
# bfs를 쓰기 위한 델타
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# 큐를 사용 => 익은 것의 주변 사방을 체크해야하므로 추가로 익은 토마토를 큐에 넣어 다시 탐색시키기 위함.
# deque를 사용안하면 시간 초과가 뜸. 아마 popleft 때문에 시간초과가 안뜨는 듯.
# 일반적인 pop(0)은 O(n), popleft는 O(1)이라고 함.
queue = deque([])

# 처음부터 익어있는 토마토 파악.
for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            queue.append([i, j])

# 큐가 비어있을 때 더 이상 새로 추가된 토마토가 없는 경우임.
while queue:
    # 큐에 먼저 들어온 순서대로 빼주기.
    i, j = queue.popleft()
    for k in range(4):
        ci = i + di[k]
        cj = j + dj[k]
        if 0 <= ci < M and 0 <= cj < N and box[ci][cj] == 0:
            # 익은 것 체크하면서 날짜도 체크하기 위해 그 전의 좌표값에 1을 더해서 저장.
            box[ci][cj] = box[i][j] + 1
            queue.append([ci, cj])

# 새로 안 것인데 2차원 배열의 max 값을 찾으려념 아래처럼 하면 됨.
result = max(map(max, box)) - 1
for i in range(M):
    for j in range(N):
        if box[i][j] == 0:
            result = -1
print(result)


