import sys
# N : 회원 수, M : 관계 수
N, M = map(int, input().split())
# W : 1~N까지의 사람들의 무게
W = [0] + list(map(int, input().split()))
# 비어있는 그래프를 만들어줌
arr = [[] for _ in range(N+1)]

# 관계 수만큼 그래프에 추가
for _ in range(M):
    x,y = map(int, input().split())
    # 양방향 관계이므로 x, y 둘 다에 append
    arr[x].append(y)
    arr[y].append(x)

# 자신이 최고라 생각하는 회원 수
result = 0

# 각각의 회원을 돌며 무게를 비교함.
for i in range(1, N+1):
    # 기본을 True로 주고 무거운걸 드는 사람이 있으면 False로 변경하려 함.
    best = True
    # 빈 arr가 있을 경우만 탐색
    if arr[i]:
        for j in arr[i]:
            # 자신보다 더 무거운 걸 들거나 같은 무게를 드는 사람이 있으면 False
            if W[i] <= W[j]:
                best = False
    if best:
        result += 1

print(result)