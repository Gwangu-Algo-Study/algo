N = int(input())
arr = list(map(int, input().split()))
# 정답 후보가 되는 순열을 담아두기 위함
sub = list(0 for _ in range(N))
# 순열로 뽑아낼 숫자가 인덱스 값이므로 인덱스 값에 방문했는지 여부를 저장하기 위함
visited = [0 for _ in range(N)]
answer = 0

# 전체 순열을 다 체크해보고, 최대값을 찾는 함수
# 거의 모든 중복 없는 순열을 만들 때는 이 함수를 사용하면 됨
def check_all(x):
    # 최대값을 저장해줄 변수
    global answer
    total = 0
    # 순열이 완성되었을 때(요소의 개수가 N개가 되었을 때)
    if x == N:
        # 제시된 식에 대입해봄
        for i in range(1, N):
            total += abs(arr[sub[i]] - arr[sub[i-1]])
        answer = max(total, answer)

    # 순열을 만들어줄 재귀함수
    for i in range(N):
        if visited[i] == 1:
            continue
        sub[x] = i
        visited[i] = 1
        check_all(x+1)
        visited[i] = 0

check_all(0)
print(answer)