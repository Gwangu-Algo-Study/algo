def solution(want, number, discount):
    answer = 0
    temp = {}
    wants = {}
    length_want = len(want)
    # 비교하기 편하게 want와 number를 이용한 dict를 하나 만들어준다.
    for i in range(length_want):
        wants[want[i]] = number[i]
    length = len(discount)
    # 10개까지만 dict 만들어준다.
    for i in range(10):
        if discount[i] in temp:
            temp[discount[i]] += 1
        else:
            temp[discount[i]] = 1
    # 목표로 하는 wants와 같은지 비교한다.
    if temp == wants:
        answer += 1
    # temp를 갱신해주며 wants와 계속 비교
    for i in range(10, length):
        if discount[i] in temp:
            temp[discount[i]] += 1
        else:
            temp[discount[i]] = 1
        temp[discount[i-10]] -= 1
        if temp[discount[i-10]] == 0:
            del temp[discount[i-10]]
        if temp == wants:
            answer += 1
        
    
    return answer