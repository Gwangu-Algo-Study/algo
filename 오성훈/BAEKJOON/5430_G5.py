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
    if n == 0:
        arr = []
    start = 0
    now = 0
    if cnt > n:
        answer[i] = 'error'
    for j in p:
        if j == 'R':
            if now == start:
                now = n-1
            else:
                now = start
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