import sys

T = int(sys.stdin.readline())
answer = [0] * T
for i in range(T):
    p = sys.stdin.readline()
    cnt = 0
    for j in p:
        if j == 'D':
            cnt += 1
    n = int(sys.stdin.readline())
    arr = list(sys.stdin.readline().strip('\n[]').split(','))
    # arr가 비어있을 때 [''] 이런식으로 나오는게 불편해서 따로 처리해 중었다. 안해도 상관 없음.
    if n == 0:
        arr = []
    start = 0
    now = 0
    # D의 개수가 배열 길이보다 크다면 무조건 error
    if cnt > n:
        answer[i] = 'error'
    for j in p:
        # 뒤집는 과정 대신 now의 위치를 배열의 첫음과 끝으로 왔다갔다 하면 된다.
        if j == 'R':
            if now == start:
                now = n-1
            else:
                now = start
        # 하나 빼는 과정 대신 양 끝부분과 now의 위치를 하나 더하거나 빼주면 된다.
        elif j == 'D':
            if now == start:
                now += 1
                start += 1
            else:
                now -= 1
                n -= 1
    if answer[i] != 'error':
        temp = '['
        if now == start:
            for j in range(start, n):
                temp += arr[j] + ','
            answer[i] = temp[:-1] + ']'
        else:
            for j in range(n-1, start-1, -1):
                temp += arr[j] + ','
            answer[i] = temp[:-1] + ']'
        if answer[i] == ']':
            answer[i] = '[]'
for i in answer:
    print(i)