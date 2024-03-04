from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 범위 체크
def check_range(x, y):
    if (x < 0 or y < 0 or x >= N or y >= M):
        return False
    else:
        return True

# 범위를 벗어나지 않고, 방문하지 않은 곳의 물인지 체크
water_visited = [list(0 for _ in range(M)) for _ in range(N)]
def can_go_water(x, y):
    if (check_range(x, y) == False):
        return False
    if (matrix[x][y] == 1 or water_visited[x][y] == 1):
        return False
    else:
        return True

# 범위를 벗어나지 않고, 방문하지 않은 곳의 빙하인지 체크
ice_visited = [list(0 for _ in range(M)) for _ in range(N)]
def can_go_ice(x, y):
    if (check_range(x, y) == False):
        return False
    if (ice_visited[x][y] == 1):
        return False
    else:
        return True

# BFS 탐색을 위해 필요한 변수들 선언
q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 외부를 둘러싸는 물 찾기 (가장 가장자리의 물, 테두리)
outer_water = set()     # -> 가장 가장자리 물의 좌표들을 담을 set()
def bfs_outer_water(q):
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if(can_go_water(new_x, new_y)):
                water_visited[new_x][new_y] = 1
                outer_water.add((new_x, new_y))
                q.append((new_x, new_y))

# 외부와 맞닿은 물이 주변에 있는지 확인 (== 빙하가 녹일 수 있는 물이 빙하와 닿아있으면 True)
def check_water(x, y):
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if(check_range(n_x, n_y) and matrix[n_x][n_y] == 0):
            if((n_x, n_y) in outer_water):
                return True
    return False

# 녹는 얼음 찾기
def bfs_ice_melt(q):
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if(can_go_ice(new_x, new_y)):
                if(check_water(new_x, new_y)):   # 주변에 빙하를 녹일 수 있는 물과 맞닿아있는지 확인
                    ice_visited[new_x][new_y] = 1
                    melting.append((new_x, new_y))
                    q.append((new_x, new_y))

# 다 녹았는지 확인하는 함수 (== 다 녹았으면 종료하기 위함)
def all_melt(m):
    for x in range(N):
        for y in range(M):
            if(m[x][y] == 1):
                return False
    return True


## Main 실행

# 맨 처음 상태의 외부와 둘러쌓인 물 구하기 (아직 빙하가 녹기 전의 테두리 물)
water_visited[0][0] = 1
outer_water.add((0, 0))
q.append((0, 0))

bfs_outer_water(q)

T = 0           # 빙하가 전부 녹는데 걸리는 시간을 담을 변수
last_ice = 0    # 마지막으로 녹은 빙하의 크기를 저장한 변수

# 빙하가 다 녹을 때까지 실행
while not (all_melt(matrix)):
    ice_visited = [list(0 for _ in range(M)) for _ in range(N)]     # 다음 빙하의 탐색을 위한 빙하 방문 처리 배열 초기화

    # 현재 존재하는 빙하들을 담아두기
    glaciers = []
    for i in range(1, N):
        for j in range(1, M):
            if (matrix[i][j] == 1):
                glaciers.append((i, j))

    # 해당 빙하들을 탐색
    for g in range(len(glaciers)):
        melting = []

        i = glaciers[g][0]
        j = glaciers[g][1]

        if(matrix[i][j] == 1 and ice_visited[i][j] == 0):       # 만약 빙하인데 방문한 적 없는 빙하라면 -> 녹음
            ice_visited[i][j] = 1
            melting.append((i, j))
            q.append((i, j))

            bfs_ice_melt(q)     # -> 해당 빙하 주변에 녹을 수 있는 빙하가 더 있는지 탐색

        # 현재 녹을 수 있는 빙하가 존재한다면 -> 녹이기
        if (melting):
            T += 1
            last_ice = 0
            for m in range(len(melting)):
                ice = melting[m]
                if(matrix[ice[0]][ice[1]] == 1):    # 빙하 녹이기
                    matrix[ice[0]][ice[1]] = 0
                    last_ice += 1

                outer_water.add((ice[0], ice[1]))   # 녹았으니까 외부 물에 추가해주기

                # 방문 처리 업데이트
                water_visited[ice[0]][ice[1]] = 1
                ice_visited[ice[0]][ice[1]] = 0

                # 현재 녹은 빙하에서 외부 테두리 물로 추가되는 물이 있는지 찾아서 업데이트
                q.append((ice[0], ice[1]))
                bfs_outer_water(q)          # 추가적인 외부 물 업데이트

# 정답 출력
print(T, last_ice)
