def solution(participant, completion):
    answer = ''
    temp = {}
    # 딕셔너리로 완주한 인원 체크
    for i in completion:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    # 참가인원과 완주한 인원 비교
    for i in participant:
        if i in temp:
            temp[i] -= 1
            if temp[i] == -1:
                answer = i
                break
        else:
            answer = i
            break
    return answer