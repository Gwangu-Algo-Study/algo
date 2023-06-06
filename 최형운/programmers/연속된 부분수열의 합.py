def solution(sequence, k):
    # 투 포인터를 이용해여 계산
    start = 0
    end = 0
    sum = 0
    answer = [0, len(sequence) - 1]
    check = 0
    # 배열 중 k 값과 같은 요소가 있는지 확인
    for i in range(len(sequence)):
        check += sequence[i]
        if sequence[i] == k:
            return [i, i]
    # 전체 합이 k 인경우
    if check == k:
        return answer
    # 진짜 투포인트 시작
    while end < len(sequence):
        # 전체 합이 k보다 클때까지 end를 1씩 늘려가며 더한다
        if sum < k:
            sum += sequence[end]
            end += 1
        # k와 값이 같고 기존의 부분수열보다 길이가 작다면 채택
        if sum == k and end - start - 1 < answer[1] - answer[0]:
            answer = [start, end - 1]
        # 합이 k보다 큰 경우에 start 포인터를 하나씩 빼간다.
        # 합이 k보다 작아 졌는데 아직도 k랑 같지 않다면 끝낸다
        while sum >= k and start < len(sequence):
            sum -= sequence[start]
            start += 1
            # k와 값이 같고 기존의 부분수열보다 길이가 작다면 채택
            if sum == k and end - start - 1 < answer[1] - answer[0]:
                answer = [start, end - 1]
    return answer