def solution(picks, minerals):
    answer = 0

    # 곡괭이 수 * 5개까지만 광물을 남기고 뒷 부분은 제거
    cnt = 0
    for p in picks :
        cnt += p
    minerals = minerals[:cnt*5]

    # 광물을 5개씩 끊어서 저장
    minerals_5 = []
    for i in range(0, len(minerals), 5) :
        minerals_5.append(minerals[i:i+5])

    # 각 그룹의 피로도를 저장할 리스트
    dis_list = []
    # 3개의 곡괭이를 사용했을 때 각 광물 그룹의 피로도 계산
    for m5 in minerals_5 :
        dis = [0, 0, 0]
        for m in m5 :
            if m == "diamond" :
                dis[0] += 1
                dis[1] += 5
                dis[2] += 25

            elif m == "iron" :
                dis[0] += 1
                dis[1] += 1
                dis[2] += 5

            else :
                dis[0] += 1
                dis[1] += 1
                dis[2] += 1
        dis_list.append(dis)

    # 돌 곡괭이를 사용했을때 기준으로 내림차순 정렬
    dis_list = sorted(dis_list, key=lambda x: x[2], reverse=True)

    # 각 곡괭이의 순서 및 수를 고려하여 최종 피로도 계산
    for dis in dis_list :
        if picks[0] > 0 :
            answer += dis[0]
            picks[0] -= 1
        elif picks[1] > 0 :
            answer += dis[1]
            picks[1] -= 1
        elif picks[2] > 0:
            answer += dis[2]
            picks[2] -= 1

    return answer

picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks, minerals))