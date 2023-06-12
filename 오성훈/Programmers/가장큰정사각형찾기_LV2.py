def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            # 정사각형을 이루려면 자기 자신이 1이어야 한다.
            if board[i][j] != 0:
                # 자기 자신을 기준으로 위, 왼쪽 위, 왼쪽이 모두 1이어야 한다.
                # 단, 세 부분의 최솟값에 1을 더해주는 방식을 사용하기 때문에 1인지 검사하는것이 아니라 0이 아닌지를 검사해야 한다.
                if board[i-1][j] != 0 and board[i-1][j-1] != 0 and board[i][j-1] != 0:
                    # 위, 왼쪽 위, 왼쪽 중 최솟값에 1을 더해주어야 한다.
                    board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
                    # 구한 값의 최댓값을 제곱하면 넓이가 되므로 answer를 통해 최댓값을 저장해준다.
                    if board[i][j] > answer:
                        answer = board[i][j]
    # 위의 방식으로는 answer가 1일때를 탐색할 수 없으므로 별도 탐색해준다.
    if answer == 0:
        for i in range(row):
            for j in range(col):
                if board[i][j] == 1:
                    answer = 1
                    break
            if answer == 1:
                break
    return answer * answer