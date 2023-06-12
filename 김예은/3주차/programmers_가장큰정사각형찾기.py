from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, board, row, col):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    area = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx > col - 1 or ny < 0 or ny > row - 1:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx, ny))
                area += 1
    return area

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

def solution(board):
    row, col = len(board), len(board[0])
    answer = 0
    for i in range(col):
        for j in range(row):
            ans = bfs(i, j, board, row, col)
            if ans:
                answer = max(ans, answer)

    return answer

print(solution(board))