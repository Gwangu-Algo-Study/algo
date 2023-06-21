from collections import deque

temp = deque()

def func(now, temp_len):
    global length, progress, speed
    if now == length:
        return
    # 앞에서부터 100보다 클 때가 되는 날을 탐색
    for i in range(1, 100):
        if progress[now] + (i*speed[now]) >= 100:
            temp.append(1)
            break
    # 그 날에 다른 기능들의 개발 상태 체크
    for j in range(now+1, length):
        if progress[j] + (i*speed[j]) >= 100:
            temp[temp_len] += 1
        else:
            func(j, temp_len+1)
            break
            

def solution(progresses, speeds):
    global length, progress, speed
    progress = progresses
    speed = speeds
    length = len(progresses)
    func(0, 0)
    answer = list(temp)
    return answer