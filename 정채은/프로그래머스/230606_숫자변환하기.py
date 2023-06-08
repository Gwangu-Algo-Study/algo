from collections import deque


def solution(x, y, n):
    # 시간초과를 대비하여 deque사용
    q = deque()
    q.append(x)

    # 계산된 수 마다 몇번의 연산을 거쳤는지 저장할 변수
    count = [0 for _ in range(y+1)]

    # 연산을 시작하기 전 이미 x가 y와 같다면 함수 종료
    if x == y :
        return 0

    while q :
        cx = q.popleft()

        # 현재 x가 y와 같다면 종료
        if cx == y:
            break

        # x와 y가 같지 않은 경우 3가지 연산 실행
        for i in range(3) :
            if i == 0:
                nx = cx + n
            elif i == 1:
                nx = cx * 2
            else :
                nx = cx * 3

            # 계산된 nx가 y와 같거나 아직 y보다 작다면
            if nx <= y:
                # 그리고 아직 방문하지 않았다면
                if count[nx] == 0:
                    # 연산 횟수 저장
                    count[nx] = count[cx] + 1
                    # deque에 nx 추가
                    q.append(nx)
    return count[y] if count[y] > 0 else -1


print(solution(10,40,5))