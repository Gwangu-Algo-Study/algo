def solution(plans):
    answer = []

    # 덜 끝낸 과제를 저장할 리스트
    notend = []

    # 먼저 시작 시간순으로 plans를 정렬한다
    plans = sorted(plans, key= lambda x: x[1])

    # hh:mm 형태의 시간을 계산하기 쉽게 mm분 형태로 수정, 문자열을 정수 형태로 수정
    for p in plans :
        hh = int(p[1][:2])
        mm = int(p[1][3:])
        p[1] = hh*60 + mm
        p[2] = int(p[2])

    for i in range(len(plans)):
        # 마지막 과제인 경우 다음 과제와 비교할 수 없으므로 notend에 바로 저장
        if i == len(plans) -1 :
            notend.append(plans[i])
            break

        # 만약 다음 과제 시간이 되기 전에 이전 과제가 끝난다면 answer에 저장
        if plans[i][1] + plans[i][2] <= plans[i+1][1] :
            answer.append(plans[i][0])

            # 과제를 끝냈는데 다음 과제 시작 시간까지 여유 시간이 남는 경우
            empty_time = plans[i+1][1] - (plans[i][1] + plans[i][2])
            while empty_time != 0 and notend :
                # 가장 최근에 멈춰둔 과제 꺼내기
                notend_sub = notend.pop()

                # 만약 비는 시간보다 멈춰둔 과제 수행 시간이 작다면 answer에 저장
                if empty_time >= notend_sub[2] :
                    answer.append(notend_sub[0])
                    empty_time -= notend_sub[2]

                # 비는 시간보다 과제 수행 시간이 크다면 비는 시간 만큼 과제 수행 시간을 줄이고 다시 notend에 저장
                else :
                    notend_sub[2] -= empty_time
                    notend.append(notend_sub)
                    empty_time = 0

        # 이전 과제를 끝내지 못했다면 notend에 남은 과제 시간을 수정하여 저장
        else :
            plans[i][2] = plans[i][2] - (plans[i+1][1] - plans[i][1])
            notend.append(plans[i])

    # 끝내지 못했던 과제들을 뒤에서부터 answer에 저장
    while notend:
        answer.append(notend.pop()[0])

    return answer



plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))