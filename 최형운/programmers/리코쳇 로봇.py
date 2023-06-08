di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def solution(board):
    answer = 0
    start = []
    n = len(board)
    m = len(board[0])
    check = [[0] * (m+2) for _ in range(n+2)]
    result = [1000000]
    board=['D'*m]+board+['D'*m]

    def move(board, i, j, n, m, count, check):
        if result[0]<=count:
            return
        else:
            if board[i][j] == 'G':
                result.pop()
                result.append(count)
                return
            for x in range(4):
                temp_i = i
                temp_j = j
                while board[temp_i][temp_j] != 'D':
                    temp_i += di[x]
                    temp_j += dj[x]
                temp_i -= di[x]
                temp_j -= dj[x]
                if check[temp_i][temp_j] == 1:
                    continue
                if board[i][j] == 'G':
                    result.pop()
                    result.append(count)
                    return
                check[temp_i][temp_j] = 1
                move(board, temp_i, temp_j, n, m, count + 1, check)
                check[temp_i][temp_j] = 0
                continue

    for i in range(len(board)):
        board[i]='D'+board[i]+'D'
        if 'R' in board[i]:
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    start.append(i)
                    start.append(j)
                    check[i][j]=1
                    break
    move(board, start[0], start[1], n+2, m+2, 0,check)
    if result[0] !=1000000:
        answer=min(result)
    else:
        answer=-1
    return answer
