import sys

N = int(sys.stdin.readline())
dp = [0] * 16 # N의 최댓값
dp[0] = 2 # 최소 사각형 변의 점 개수


for i in range(1,N+1):
    dp[i] = dp[i-1] + (dp[i-1] -1)

print(dp[N]**2)
