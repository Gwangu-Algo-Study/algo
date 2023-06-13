from collections import deque

N, M = map(int, input().split())

member = [[] for _ in range(N+1)]
# 한 사람 분의 케빈 베이컨의 수 구하는 함수
def find_member(a):
    # visited는 방문 여부가 아닌 방문하기까지 걸린 친구의 수를 뜻함
    visited = [0 for _ in range(N+1)]
    queue = deque([a])
    while queue:
        man = queue.popleft()

        # 몇명을 거쳐서 왔는지 저장해야 하므로 visited[man] + 1 을 저장해줌
        for k in member[man]:
            if visited[k] == 0:
                visited[k] = visited[man] + 1
                queue.append(k)

        # 가장 작은 것을 구해야 하므로 list의 합을 돌려줌
    return sum(visited)


# 친구의 방향을 2차원 배열에 저장해줌.
for _ in range(M):
    x, y = map(int, input().split())
    member[x].append(y)
    member[y].append(x)

# 최소 값을 찾아야 하므로.
answer = 0
answer_cnt = 5000000000
for i in range(1, N+1):
    result = find_member(i)
    if result < answer_cnt:
        answer = i
        answer_cnt = result

print(answer)