def solution(storey):
    answer = 0
    storey=str(storey)
    floor = [int(i) for i in storey]
    # 조건 비교를 위해 자릿수 별로 쪼개고 int 형태로 리스트에 저장
    # 리스트 뒤에서 부터 시작
    for i in range(1,len(floor)+1):
        # 맨 앞(가장 큰 자릿수의 값)이 10이 넘는 경우
        if i == len(floor) and floor[0]>=10:
            answer+=floor[0]%10+floor[0]//10
            break
        # 맨 앞이 5보다 크면 올라갔다가 내려가는 경우
        elif i == len(floor) and floor[0]>5:
            answer+=10-floor[0]+1
            break
        # 5일 경우에 다음 자릿수에 따라 올릴지 말지를 결정
        elif floor[-i]==5 and i != len(floor) and floor[-i-1]>=5:
            answer+=10-floor[-i]
            floor[-i] = 0
            #다음 자릿수가 10이 되면 다다음 자릿수에 1추가
            if floor[-i-1]+1==10 and i < len(floor)-1:
                floor[-i-2]+=1
                floor[-i-1]=0
            #아니면 그냥 하던데로
            else:
                floor[-i-1]+=1
        # 5보다 크면 위에 있던 올라간다.
        elif floor[-i]>5 and i != len(floor):
            answer+=10-floor[-i]
            floor[-i] = 0
            if floor[-i-1]+1==10 and i < len(floor)-1:
                floor[-i-2]+=1
                floor[-i-1]=0
            else:
                floor[-i-1]+=1
        else:
            answer+=floor[-i]
            floor[-i]=0
    return answer