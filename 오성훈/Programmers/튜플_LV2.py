def solution(s):
    # ","를 기준으로 끊으면 {}가 붙어있는 숫자들이 생긴다.
    s = s.split(',')
    length = len(s)
    temp = {}
    for i in range(length):
        # 붙어있는 {}를 떼어준다.
        s[i] = int(s[i].strip('{}'))
        # 정렬을 위해 개수가 필요하니 dict를 통해 세어준다.
        if s[i] in temp:
            temp[s[i]] += 1
        else:
            temp[s[i]] = 1
    # 개수에 따라 정렬시켜준다.
    answer = sorted(temp.items(), key = lambda x : x[1], reverse=True)
    length = len(answer)
    # 요구사항에 맞게 answer의 구조를 변경한다.
    for i in range(length):
        answer[i] = answer[i][0]
    return answer