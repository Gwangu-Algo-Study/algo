from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # 중요도 순서의 queue
    arr = deque(list(map(int, input().split())))
    # 인덱스 순서의 queue
    queue = deque([i for i in range(N)])
    # 몇 번째로 인쇄됐는지 알아야 하므로 1부터 시작
    result = 1

    # queue가 존재하는 동안 계속 수행해야함.
    while arr:
        # x : 중요도, y : 인덱스
        # 중요도와 인덱스 2개의 정보 모두 활용해야 하므로.
        x = arr.popleft()
        y = queue.popleft()

        # 1개가 남아있을 경우의 예외처리를 위해 len(arr) > 0을 넣어줌
        # 1개 남을 경우 popleft를 하면 arr가 존재하지 않기 때문
        if len(arr) > 0 and x < max(arr):
            arr.append(x)
            queue.append(y)
        else:
            # 찾아야할 인덱스가 나올 경우 while문 종료
            if y == M:
                print(result)
                break
            else:
                result += 1