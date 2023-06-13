def solution(n):
    answer = 0
    a=[0,1]
    i=0
    while len(a)!=n+1:
        a.append(a[i]+a[i+1])
        i+=1
    answer=a[-1]%1234567
    return answer