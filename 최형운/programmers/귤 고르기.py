import collections
# 리스트의 중복갯수를 딕셔너리로 바꾸기 위해 collections를 사용
def solution(k, tangerine):
    answer = 0
    tanger_list=sorted(collections.Counter(tangerine).values(),reverse=True)
    # 중복갯수를 구하고 중복된 갯수들만 추출, 많은 수를 가지고 있는 순서로 정렬
    kind=0
    for i in tanger_list:
        kind+=i
        answer+=1
        # 상자에 많은 양 순서로 담고 갯수를 더한다.
        if kind>=k:
        # 원하는 양을 채웠으면 끝낸다
            break
    return answer