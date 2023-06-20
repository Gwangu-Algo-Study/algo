def solution(brown, yellow):
    answer = [0] * 2
    for i in range(1, yellow+1):
        if yellow%i == 0:
            j = yellow//i
            if i >= j and j*2 + i*2 + 4 == brown:
                answer[0] = i+2
                answer[1] = j+2
                break
    return answer