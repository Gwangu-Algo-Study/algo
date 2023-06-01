import math

# 숫자 조합의 개수 파악
def find_number_combination(target):
    target_sqrt = int(math.sqrt(target))
    for i in range(target_sqrt, 0, -1):
        if arr[target] > arr[i*i] + arr[target - (i*i)]:
            arr[target] = arr[i*i] + arr[target - (i*i)]


target = int(input())
# arr는 각 인덱스를 만드는 숫자 조합의 최소 개수
arr = [5] * 50001
arr[1] = 1
arr[2] = 2
arr[3] = 3

# 루트 50000 = 223.XX 이므로 223까지 
for i in range(2, 224) :
    arr[i*i] = 1

for i in range(5, target+1):
    find_number_combination(i)
print(arr[target])