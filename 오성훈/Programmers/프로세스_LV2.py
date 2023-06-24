from collections import deque
def solution(priorities, location):
    answer = 0
    # que를 통해 시뮬레이션
    que = deque(priorities)
    # 정렬을 통해 남은 수 중 최댓값 찾기
    priority = sorted(priorities)
    length = len(priorities)
    for i in range(length-1, -1, -1):
        temp = 0
        for j in que:
            # 최댓값 찾으면 answer 1 증가, 반복 중지
            if j == priority[i]:
                answer += 1
                if location == 0:
                    location = -2
                    break
                location -= 1
                if location == -1:
                    location = len(que)-1
                break
            # 최댓값 못찾으면 rotate(회전)시킬 temp 값 1 증가
            else:
                temp += 1
                location -= 1
                if location == -1:
                    location = len(que)-1
            print(que)
        que.rotate(-temp)
        que.popleft()
        if location == -2:
            break
    return answer