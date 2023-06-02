import sys
from collections import deque

# 조금이나마 시간을 줄여보고자 sys 이용
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
paper = [0] * 3   # 순서대로 0, 1, -1 종이의 개수
stack = deque()
stack.append([N, 0, 0, N, N])   # 길이, start_y, start_x, end_y, end_x

# 조금이나마 시간을 줄여보고자 재귀 대신 스택으로 구현
while stack:
    length, sy, sx, ey, ex = stack.pop()
    temp = arr[sy][sx]
    flag = 0
    for i in range(sy, ey):
        for j in range(sx, ex):
            if arr[i][j] != temp:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        if temp == -1:
            paper[2] += 1
        else:
            paper[temp] += 1
    else:
        # 가로 / 세로 순서로 표시함
        stack.append([length//3, sy, sx, sy+length//3, sx+length//3])   # 왼쪽 / 위
        stack.append([length//3, sy, sx+length//3, sy+length//3, sx+length//3*2])   # 가운데 / 위
        stack.append([length//3, sy, sx+length//3*2, sy+length//3, ex])   # 오른쪽 / 위
        stack.append([length//3, sy+length//3, sx, sy+length//3*2, sx+length//3])   # 왼쪽 / 가운데
        stack.append([length//3, sy+length//3, sx+length//3, sy+length//3*2, sx+length//3*2])   # 가운데 / 가운데
        stack.append([length//3, sy+length//3, sx+length//3*2, sy+length//3*2, ex])   # 오른쪽 / 가운데
        stack.append([length//3, sy+length//3*2, sx, ey, sx+length//3])   # 왼쪽 / 아래
        stack.append([length//3, sy+length//3*2, sx+length//3, ey, sx+length//3*2])   # 가운데 / 아래
        stack.append([length//3, sy+length//3*2, sx+length//3*2, ey, ex])   # 오른쪽 / 아래
    
print(paper[2])
print(paper[0])
print(paper[1])