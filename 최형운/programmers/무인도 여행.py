DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
def solution(maps):
    MAX_R, MAX_C = len(maps), len(maps[0])  # 지도의 행과 열의 크기

    def dfs(start_r, start_c, start_count):
        nonlocal visited  # 외부 함수의 visited 변수에 접근하기 위해 nonlocal 선언

        stack = [(start_r, start_c)]
        visited[start_r][start_c] = True
        counts = start_count
        while stack:
            curr_r, curr_c = stack.pop()
            for dir_r, dir_c in DIRS:
                post_r, post_c = curr_r + dir_r, curr_c + dir_c
                if 0 <= post_r < MAX_R and 0 <= post_c < MAX_C and maps[post_r][post_c] != 'X' and not visited[post_r][post_c]:
                    visited[post_r][post_c] = True
                    counts += int(maps[post_r][post_c])
                    stack.append((post_r, post_c))

        return counts

    islands = []  # 섬에서 최대 며칠 머물 수 있는지를 저장할 리스트
    visited = [[False] * MAX_C for _ in range(MAX_R)]  # 방문 여부를 저장하는 2차원 리스트
    for r in range(MAX_R):
        for c in range(MAX_C):
            if maps[r][c] != 'X' and not visited[r][c]:  # 땅이면서 아직 방문하지 않은 경우
                islands.append(dfs(r, c, int(maps[r][c])))  # dfs 탐색을 통해 섬의 최대 며칠 머물 수 있는지 계산

    return sorted(islands) if islands else [-1]  # 오름차순으로 정렬하여 반환하고, 섬이 없는 경우 -1을 반환

a=["X591X","X1X5X","X231X", "1XXX1"]
print(solution(a))