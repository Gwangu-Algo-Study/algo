from collections import deque


def solution(n, roads, sources, destination):
    # 방문 여부를 저장하는 리스트
    visit = [-1] * (n + 1)

    # 각 지역의 인접한 지역을 저장하는 그래프
    graph = [[] for _ in range(n + 1)]

    # 길 정보를 바탕으로 그래프 생성
    for s, e in roads:
        # 양방향 그래프이므로 양쪽으로 간선 추가
        graph[s].append(e)
        graph[e].append(s)

    # 목적지부터 출발하여 BFS를 수행하여 최단 시간을 계산
    Q = deque([destination])
    visit[destination] = 0
    while Q:
        now = Q.popleft()

        # 현재 지역과 인접한 지역들을 확인
        for node in graph[now]:
            if visit[node] == -1:
                # 방문하지 않은 지역이라면
                # 현재 지역에서 해당 지역까지의 최단 시간을 계산하여 저장
                visit[node] = visit[now] + 1
                Q.append(node)

    # 각 부대원의 최단 시간을 반환
    return [visit[i] for i in sources]