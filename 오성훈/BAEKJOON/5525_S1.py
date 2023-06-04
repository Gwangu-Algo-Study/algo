
N = int(input())
M = int(input())
S = input()
last = M-(2 * N + 1) + 1
answer = 0
now = 0
while now < last:
    i = -1
    for j in range(now, last):
        if S[j] == 'I':
            i = j
            break
    if i == -1:
        break
    cnt = 0
    for j in range(i, M-2, 2):
        if S[j] == 'I' and S[j+1] == 'O':
            cnt += 1
        else:
            break
        if cnt >= N and S[j+2] == 'I':
            answer += 1
    now = j + 1
print(answer)