def solution(dirs):
    answer = set()

    # dict 형식으로 지정하여 글자별로 꺼내기 쉽게 사용
    d = {"U" : [0,1], "D" : [0,-1], "R" : [1,0], "L" : [-1,0]}

    x, y = 0, 0

    for i in dirs :
        nx = x + d[i][0]
        ny = y + d[i][1]

        # nx와 ny가 범위 안에 있다면
        if -5 <= nx <= 5 and -5 <= ny <= 5 :
            # (현재위치, 이동위치)와 (이동위치, 현재위치)를 set에 넣기
            # 한 번 간 길을 돌아오더라도 이미 거긴 간 길이므로 set에 같이 추가해주는 것
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x, y = nx, ny
    return len(answer)//2

dirs = "ULURRDLLU"
print(solution(dirs))