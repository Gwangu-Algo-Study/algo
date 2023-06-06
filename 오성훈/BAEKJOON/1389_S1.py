import sys
n, m = map(int, sys.stdin.readline().split())
relation = [[999999] * (n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    relation[x][y] = 1
    relation[y][x] = 1

# 플로이드 워셜
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            for k in range(1, n+1):
                relation[j][k] = min(relation[j][k], relation[j][i] + relation[i][k])
                relation[k][j] = min(relation[j][k], relation[j][i] + relation[i][k])


# 케빈 베이컨의 수가 가장 적은 사람 찾기
minimum = 999999999
minimum_person = -1
for i in range(1, n+1):
    if sum(relation[i]) < minimum:
          minimum = sum(relation[i])
          minimum_person = i
print(minimum_person)