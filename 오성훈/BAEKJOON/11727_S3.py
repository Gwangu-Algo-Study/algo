n = int(input())

arr = [0] * 1001
arr[1] = 1
arr[2] = 3
for i in range(3, n):
    arr[i] = arr[i-1] + arr[i-2] * 2
if n > 2:
    print((arr[n-1] + arr[n-2] * 2)%10007)
else:
    print(arr[n])