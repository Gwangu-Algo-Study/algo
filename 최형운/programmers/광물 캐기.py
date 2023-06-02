def solution(picks, minerals):
    result = 0
    five=[]
    # 한번 선택한 곡괭이는 5개를 꼭 캐야되기 때문에 광물을 5단위로 끊습니다.
    for i in range(0,len(minerals),5):
        check=[0,0,0]
        for j in range(5):
            if i+j<len(minerals):
                #편의를 위해 다이아는 0. 철은 1, 돌은 2 인덱스에 갯수를 저장합니다.
                if minerals[i+j]=="diamond":
                    check[0]+=1
                elif minerals[i+j]=="iron":
                    check[1]+=1
                elif minerals[i+j]=="stone":
                    check[2]+=1
        #곡괭이가 없으면 어차피 못캐니까 곡괭이 갯수가 넘지 않게 합니다.
        if sum(picks)>len(five):
            five.append(check)
        else:
            break
    # 다이아를 기준으로 정렬하고 그 안에서 철을 기준으로 정렬합니다.
    five=sorted(five,key=lambda x:(-x[0],-x[1]))
    while len(five) !=0 and sum(picks) !=0:
        if len(five) !=0:
            today=five.pop(0)
            # 다이아 곡괭이가 있다면
            if picks[0] !=0:
                print(sum(today))
                result+=sum(today)
                picks[0]-=1
            # 다이아 곡괭이가 없고 철 곡괭이가 있다면
            elif picks[1] !=0:
                result+=5*today[0]+1*today[1]+1*today[2]
                picks[1]-=1
            # 돌 곡괭이만 있다면
            else:
                result+=25*today[0]+5*today[1]+1*today[2]
                picks[2]-=1
    return result