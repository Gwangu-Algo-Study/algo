def solution(participant, completion):
    runners = {}
    # 참가자의 명단을 딕셔너리에 추가해준다.
    for i in participant:
        if i in runners:
            # 참가자가 있다면 1을 더해준다.
            runners[i] += 1
        else:  # 참가자가 없다면 기본 값인 1이다
            runners[i] = 1

    for j in completion:
        if j in runners:
            runners[j] -= 1
        else:
            continue

    for key, value in runners.items():
        # 만약 value값이 0이 아니라면, -> completion에 없다면
        if value != 0:
            #         그 범인이 바로 미완주자입니다.
            answer = str(key)

    return answer