import math
def solution(r1, r2):
    answer = 0
    # 그래프의 한 사분면만 고려
    for i in range(1, r2):
        a = (r1**2 - i**2) if r1 > i else 0
        b = int(math.sqrt(a))
        c = int(math.sqrt(r2**2 - i**2))
        # x 좌표값에 대한 점의 개수
        answer += c - b + (1 if b ** 2 == a else 0)
    # x 좌표값 = r2 일 때
    answer += 1
    return answer * 4