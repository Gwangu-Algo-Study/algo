def solution(phone_book):
    answer = True
    temp = {}
    # 각 전화번호 딕셔너리에 저장
    for i in phone_book:
        temp[i] = 1
    total_length = len(phone_book)
    # 최대 전화번호 길이가 20이므로 앞에서부터 자르며 딕셔너리에 있는지 확인
    for i in range(total_length):
        length = len(phone_book[i])
        for j in range(1, length):
            if phone_book[i][:j] in temp:
                answer = False
                break
        if answer == False:
            break        
    return answer