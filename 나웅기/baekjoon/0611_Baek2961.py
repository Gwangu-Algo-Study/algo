N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1000000001

# x : arr의 자리 수, cnt : 들어간 재료 수, s : 신 맛의 크기, b : 쓴 맛의 크기
def check_all(x, cnt, s, b):
    global ans
    # 문제에서 재료를 적어도 하나를 사용했을 경우라 나왔으므로
    # 하나만 고른 것부터 전부 고른 경우까지 모두 탐색을 해야하므로
    # 0이 아닌 경우 결과 값으로 저장해줌
    if cnt != 0:
        ans = min(ans, abs(s-b))

    # 아무것도 선택하지 않았을 때는 그냥 종료
    if x == N:
        return

    # 아래는 선택했을 경우와 안했을 경우를 재귀로 돌림
    # 재료를 선택한 경우
    check_all(x+1, cnt + 1, s * arr[x][0], b + arr[x][1])
    # 재료를 선택하지 않은 경우
    check_all(x+1, cnt, s, b)

# 신 맛은 곱하기 이므로 1부터 시작
check_all(0, 0, 1, 0)
print(ans)