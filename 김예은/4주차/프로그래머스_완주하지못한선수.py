
par
def solution(participant, completion):
    runners = {}
    # 참가자의 명단을 딕셔너리에 추가해준다.
    for i in participant:
        runners[i] += 1

    for key, value in runners.items():
        for j in completion:
            if key == j:
                runners[key] -= 1
        if value == 0:
            answer = value

    return answer