def solution(clothes):
    clothes_dict = {}
    answer = 1
    for i in clothes:
        # 옷 종류가 있을 때
        if i[1] in clothes_dict:
            # 옷 종류 개수에 1을 더해준다.
            clothes_dict[i[1]] += 1
        else: #옷 종류가 없다면 기본값인 1이다.
            clothes_dict[i[1]] = 1
    for i in clothes_dict.values():
        # 조합의 경우의 수는 n차식 계수들의 합인데,
        #(1+a)(1+b)(1+c) -1의 값으로 구할 수 있다.
        answer *= (i+1)
    return answer -1