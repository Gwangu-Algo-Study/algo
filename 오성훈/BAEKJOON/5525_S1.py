
N = int(input())
M = int(input())
S = input()
# 탐색할때 남은 문자열의 길이가 2*N+1 보다 짧다면 탐색할 필요가 없다.
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
    # I를 찾은 구간부터 IO를 탐색하가며 카운트한다.
    # IO가 N보다 많아지면서 그 다음칸도 I면 문자열 P가 완성이 된 것이기에 answer에 1개 더해준다.
    for j in range(i, M-2, 2):
        if S[j] == 'I' and S[j+1] == 'O':
            cnt += 1
        else:
            break
        if cnt >= N and S[j+2] == 'I':
            answer += 1
    now = j + 1
print(answer)