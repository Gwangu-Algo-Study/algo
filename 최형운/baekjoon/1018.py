m,n=map(int,input().split())
pan=[input() for _ in range(m)]
arr, arr_white, arr_black=[[0]*n for _ in range(m)],[[0]*n for _ in range(m)],[[0]*n for _ in range(m)]
ws,bs='B','W'
result=100
white_sum, black_sum=0,0
for i in range(m):
    for j in range(n):
        if ws=='W':
            ws='B'
        else:
            ws='W'
        if bs=='B':
            bs='W'
        else:
            bs='B'
        if pan[i][j] != ws:
            arr_white[i][j]=1
        if pan[i][j] != bs:
            arr_black[i][j]=1
    if n%2==0:
        if ws == 'W':
            ws = 'B'
        else:
            ws = 'W'
        if bs == 'B':
            bs = 'W'
        else:
            bs = 'B'
for i in range(m-7):
    for j in range(n-7):
        for y in range(8):
            for x in range(8):
                white_sum+=arr_white[i+y][j+x]
                black_sum+=arr_black[i+y][j+x]
        if result>white_sum:
            result=white_sum
        if result>black_sum:
            result=black_sum
        white_sum,black_sum=0,0
print(result)