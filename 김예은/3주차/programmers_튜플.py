def solution(s):
    answer = []
    
    # 문자열 처리1: [2:-2]를 통해 맨 앞, 맨 뒤 "{","}" 제거 후 "},{"로 split
    splitted = s[2:-2].split("},{") 
    
    # 문자열 처리2: 각 내부 원소를 "," 기준으로 split하고, 튜플 길이에 따라 정렬
    splitted2 = sorted([spl.split(',') for spl in splitted], key=lambda x:len(x))

    answer.append(int(splitted2[0][0]))     # 가장 짧은 튜플 원소 answer에 넣고
    for i in range(1, len(splitted2)):      # 반복문을 통해 이전 튜플에 없었던 새 값 찾아서
        for s in splitted2[i]:              # answer에 추가
            if s not in splitted2[i-1]:
                answer.append(int(s))
                break

    return answer