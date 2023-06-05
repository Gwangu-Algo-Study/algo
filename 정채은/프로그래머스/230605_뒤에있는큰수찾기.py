def solution(numbers):
    stack = []
    answer = []

    # 배열을 거꾸로 순회(시간 복잡도 개선)
    for i in range(len(numbers) - 1, -1, -1):
        while stack:
            # 스택의 top이 numbers[i]보다 작으면 스택에서 제거
            if stack[-1] > numbers[i]:
                # 스택의 top이 더 크면 answer에 추가
                answer.append(stack[-1])
                break
            stack.pop()

        # 스택이 비어있는 경우
        if not stack:
            answer.append(-1)

        stack.append(numbers[i])

    # 결과 배열 뒤집기
    answer.reverse()

    return answer

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))
