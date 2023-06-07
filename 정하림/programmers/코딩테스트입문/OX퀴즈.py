def solution(quiz):
    answer = []
    for q in quiz:
        numbers = q.split() # 숫자 혹은 기호를 담은 배열을 만든다.
        num1, num2, result = int(numbers[0]), int(numbers[2]), int(numbers[4])
        if numbers[1] == "+" :
            answer.append("O") if result == num1 + num2 else answer.append("X")
        else :    
            answer.append("O") if result == num1 - num2 else answer.append("X")
    return answer