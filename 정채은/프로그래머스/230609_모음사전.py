from itertools import product

def solution(word):
    # 조합 가능한 모든 단어를 저장할 배열
    words = []
    # 한 글자부터 다섯 글자까지
    for i in range(1, 6):
        # i번씩 반복하면서 중복 가능한 모든 순열 생성
        for w in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            # join하여 words에 추가
            words.append(''.join(w))

    # 사전순으로 정렬
    words.sort()
    # 인덱스값이 찾아지므로 +1하여 return
    return words.index(word) + 1

word = "AAAAE"
print(solution(word))