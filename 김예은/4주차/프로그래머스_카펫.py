def solution(brown, yellow):
    answer = []
    total = brown + yellow
    # 노랑이 중앙에 오려면 최소 세로크기는 3
    row = 3

    while True:
        if (total % row == 0):  # 나누어 떨어지면(가로길이라면)
            # 카펫 가장자리 제외한 부분의 크기와 노란색 격자의 갯수가 동일한지
            if (total // row - 2) * (row - 2) == yellow:
                answer.append([total // row, row])
        row = row + 1

        if (total / row) < row:
            break
    return answer[-1]