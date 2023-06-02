import sys
# 계산하기 쉽게 시간을 분으로 바꿉니다
def minute(clock):
    return int(clock[:2]) * 60 + int(clock[-2:])

def solution(plans):
    answer = []
    ing = []
    time = 0
    # 빠른 시간순으로 시작하기 위해서 빠른 시간대 순으로 정렬합니다.
    plans = sorted(plans, key=lambda x: x[1])
    # 계산하기 쉽게 시간, 과제 소요시간을 바꿉니다.
    for i in range(len(plans)):
        plans[i][1] = minute(plans[i][1])
        plans[i][2] = int(plans[i][2])
    # 반복문을 돌며 과제를 합니다.
    for i in range(len(plans)):
        # 뒤에 할 과제랑 비교할거기 때문에 마지막거는 빼줍니다.
        if i != len(plans) - 1:
            # 과제를 다했을때 시간이 다음꺼 시작시간보다 크다면 완료 못하고 정지한 상태이기 때문에 잔여 시간과 함께 진행중 목록에 추가해줍니다.
            if plans[i][1] + plans[i][2] > plans[i + 1][1]:
                ing.append([plans[i][0], plans[i][2] - (plans[i + 1][1] - plans[i][1])])
                time = plans[i][1] + plans[i][2]

            else:
                # 과제를 마무리한 시간이 다음 과제할 시간보다 적거나 같으면 완료한거기 때문에 완료 목록에 넣어줍니다.
                answer.append(plans[i][0])
                time = plans[i][1] + plans[i][2]
                # 과제를 마무리 하고도 다음 과제 시간보다 여유가 있다면 진행중인 과제를 시행합니다.
                while time < plans[i + 1][1] and len(ing) > 0:
                    a = ing.pop(-1)
                    # 진행중인 과제를 다한 시간이 다음 과제 시작시간보다 적다면 완료한거기 때문에 완료 목록에 넣어줍니다.
                    if a[1] + time <= plans[i + 1][1]:
                        answer.append(a[0])
                        time += a[1]
                    # 아니라면 소요된 시간을 제외하고 다시 진행중 목록에 넣습니다.
                    else:
                        a[1] -= (plans[i + 1][1] - time)
                        time = plans[i + 1][1]
                        ing.append(a)
        # 마지막 과제를 합니다.
        else:
            answer.append(plans[-1][0])
            # 그리고 완료하지 못한 과제들을 마저 다합니다.
            if len(ing) > 0:
                for i in reversed(ing):
                    answer.append(i[0])
    return answer