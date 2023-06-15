from collections import deque
def solution(clothes):
    answer = 0
    length = len(clothes)
    # temp에 옷의 종류의 개수를 각각 저장 예) 옷 2개, 바지 2개, 모자 3개 등
    temp = {}
    # 어떤 옷 종류가 있는지 알기 편할려고 clothes_list 만들어줌
    clothes_list = deque()
    for i in range(length):
        # 각가의 옷 종류마다 개수 파악
        if clothes[i][1] in temp:
            temp[clothes[i][1]] += 1
        else:
            temp[clothes[i][1]] = 1
            clothes_list.append(clothes[i][1])
    # 옷 종류의 개수를 이용해서 모든 경우의 수가 몇개인지 계산
    while clothes_list:
        now = clothes_list.pop()
        temp_result = temp[now]
        for i in clothes_list:
            temp_result = temp_result * (temp[i]+1)
        answer += temp_result
    return answer