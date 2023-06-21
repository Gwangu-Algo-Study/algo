def solution(book_time):
    answer = 0
    room=[]
    book_time=sorted(book_time,key=lambda x : (x[0],x[1]))
    # 입실시간을 기준으로 정렬을 합니다. 입실시간이 같다면 퇴실시간으로 합니다.
    for i in book_time:
        i=[int(i[0][:2])*60+int(i[0][-2:]),int(i[1][:2])*60+int(i[1][-2:])]
        #시간을 더하고 비교하기 위해 분단위로 만듭니다.
        check=0
        if len(room) == 0:
            # 아무것도 없다면 일단 추가
            room.append([i[0],i[1]+10])
        else:
            for j in range(len(room)):
            # 현 손님있는 방의 시간을 비교하면서 입실가능여부를 확인합니다.
                if room[j][1]<=i[0]:
                # 입실 가능하다면
                    room[j]=[i[0],i[1]+10]
                    check=1
                    break
            if check==0:
            # 기존방에 나간사람이 없다면 새방을 줍니다.
                room.append([i[0],i[1]+10])
    answer=len(room)
    return answer