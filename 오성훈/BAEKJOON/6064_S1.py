import sys

n = int(sys.stdin.readline())
cnt = [0] * n

for i in range(n):
    M, N, x, y = map(int, sys.stdin.readline().split())
    # M과  N이 같으면 x, y도 같아야 한다. 아닐 경우 -1
    if M == N:
        if x != y:
            cnt[i] = -1
        else:
            cnt[i] = x
    else:
        # x와 y는 M과 N이라는 한계치만 다르고 규칙은 똑같다.(무조건 + 1) 
        # 따라서 편의에 따라 순서를 바꿔도 상관 없다.
        if M > N:
            M, N = N, M
            x, y = y, x
        # 현재 해의 now_x는 x로 고정시키고  now_y만을 y가 될때까지 변화시킨다.
        dif = N-M
        cnt[i] = x
        now_y = x
        while now_y != y:
            cnt[i] += M
            now_y -= dif
            if now_y < 1:
                now_y = N + now_y
            # now_y가 초기값인 x로 돌아왔다는 것은 한바퀴를 돌았다는 것.
            # 마지막 해인 M:N을 지났으므로 유효하지 않은 표현. -1
            if now_y == x:
                cnt[i] = -1
                break
for i in range(n):
    print(cnt[i])
                
