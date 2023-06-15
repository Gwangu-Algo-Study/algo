def solution(cacheSize, cities):
    answer = 0
    length = len(cities)
    cache = []
    # 캐시 사이즈가 0이면 무조건 5초씩 걸림
    if cacheSize == 0:
        answer = length * 5
    else:
        # 캐시 안에 있으면 1초, 없으면 5초 걸림
        for i in range(length):
            if cities[i].lower() in cache:
                cache.pop(cache.index(cities[i].lower()))
                answer += 1
            else:
                if len(cache) == cacheSize:
                    cache.pop(0)
                answer += 5
            cache.append(cities[i].lower())
    return answer