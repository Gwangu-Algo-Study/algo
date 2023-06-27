N = int(input())
numlist = list(map(int,input().split()))
M = int(input())
compare_list = list(map(int,input().split()))

dic = {}

for num in numlist:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

# 만약 딕셔너리의 키값이 있다면, 그 밸류 값을 print하도록 해야함
answer = []
for c_num in compare_list:
    if dic.get(c_num):
        answer.append(dic.get(c_num))
    else:
        answer.append(0)
print(*answer)
