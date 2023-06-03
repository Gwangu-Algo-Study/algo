import sys

n = int(sys.stdin.readline())
cnt = [0] * n
for i in range(n):
    M, N, x, y = map(int, sys.stdin.readline().split())
    if M == N:
        if x != y:
            cnt[i] = -1
        else:
            cnt[i] = x
    else:
        if M > N:
            M, N = N, M
            x, y = y, x
        dif = N-M
        cnt[i] = x
        now_y = x
        while now_y != y:
            cnt[i] += M
            now_y -= dif
            if now_y < 1:
                now_y = N + now_y
            if now_y == x:
                cnt[i] = -1
                break
for i in range(n):
    print(cnt[i])
                
