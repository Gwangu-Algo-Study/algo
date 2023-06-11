k = int(input())
inq = input().split()

# 순열이 될 arr
arr = [0 for _ in range(k+1)]

# 0~9의 숫자가 중복되지 않도록 visited를 만들어줌
visited = [0 for _ in range(10)]

# 정답 후보인 순열을 모을 answer
answer = []

# 순열을 만들어줄 함수
def check_num(x):
    # 부등호의 수 + 1의 크기인 순열로 만들어지므로 k+1일 때 종료시킴
    if x == k+1:
        # 부등호 배열을 탐색해서 조건에 맞지 않다면 함수를 종료시킴
        for i in range(k):
            if inq[i] == "<" and (arr[i] > arr[i+1]):
                return
            if inq[i] == ">" and (arr[i] < arr[i+1]):
                return
        # 위의 작업으로 조건에 맞는 순열만 answer에 담아줌.
        # arr[:]을 하는 이유는 arr로 바로 넣게 되면 arr값이 변할 때마다 answer에 추가된 값도 함께 변해버림
        # 때문에 arr을 복사하여 넣어주어야 함.
        answer.append(arr[:])
        return

    # 순열을 만드는 부분
    for i in range(10):
        # visited가 1이라면 이는 이미 사용된 숫자이므로 그냥 통과
        if visited[i] == 1:
            continue
        # 사용되지 않은 숫자라면 arr에 넣어주고, visited도 1로 바꾸어줌
        arr[x] = i
        visited[i] = 1
        # 재귀를 돌리기 위함.
        check_num(x+1)
        # 다음 숫자에는 다른 visited를 사용해야하므로 visited를 0으로 초기화
        visited[i] = 0

check_num(0)

# 이미 순열을 만들 때 작은 숫자부터 만들어지므로 정렬할 필요 없음.
# 맨 앞과 맨 끝 값만으로 사용 가능
print(''.join(map(str, answer[-1])))
print(''.join(map(str, answer[0])))

# import sys
# input = sys.stdin.readline
# from itertools import permutations
# k = int(input())
# E = list(map(str, input().split()))
# ans = []
# num = [i for i in range(10)]
#
# for per in permutations(num, k+1):
#     for i in range(k):
#         if E[i] == "<":
#             if per[i] > per[i+1]: break
#         else:
#             if per[i] < per[i+1]: break
#     else:
#         ans.append(per)
# ans.sort()
# print(''.join(map(str, ans[-1])))
# print(''.join(map(str, ans[0])))
