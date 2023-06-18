def solution(phone_book):
    dic = {}
    for num in phone_book:
        # 각 전화번호를 key값으로 추가해줍니다.
        dic[num] = 1

        # 각 폰 번호에 대해
    for n in phone_book:  # ex. 123
        str_num = ''
        for i in n:  # ex. 1/ 2/ 3
            # 전화번호를 하나씩 추가해주면서 확인을 해봅니다. (1, 12, 123 ...)
            str_num += i
            # 하나씩 자른게 딕셔너리에 있는지 확인 (단, 본인은 아닌거)
            if (str_num in dic) and (str_num != n):
                return False  # 처음에 answer=True 하고 return answer해도 되지만 이게 더 빠름
    return True