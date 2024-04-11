import copy
from collections import deque

N, Q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(2 ** N)]
rotate_lev = list(map(int, input().split()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def check_range(x, y):
    if(x < 0 or y < 0 or x >= 2**N or y >= 2**N):
        return False
    return True


def bfs():
    group = 0
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        group += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(check_range(nx, ny) and matrix[nx][ny] != 0 and visited[nx][ny] == 0):
                visited[nx][ny] = 1
                q.append((nx, ny))

    return group


for q in range(len(rotate_lev)):
    new_matrix = copy.deepcopy(matrix)

    curr_lev = rotate_lev[q]        # 현재 선택된 레벨
    to_select = 2 ** curr_lev       # 해당 레벨에 따른 선택되는 격자 길이

    # 회전
    for i in range(0, len(matrix), to_select):
        for j in range(0, len(matrix), to_select):
            # 각 사각형 시작점 : (i, j)
            for x in range(to_select):
                for y in range(to_select):
                    new_matrix[i + x][j + y] = matrix[i + to_select - 1 - y][j + x]

    matrix = copy.deepcopy(new_matrix)

    # 녹을 얼음 파악
    to_melt = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] != 0):
                ice_cnt = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if(check_range(ni, nj) and matrix[ni][nj] != 0):
                        ice_cnt += 1
                if(ice_cnt < 3):
                    to_melt.append((i, j))

    # 동시에 녹이기
    for i in range(len(to_melt)):
        matrix[to_melt[i][0]][to_melt[i][1]] -= 1


q = deque()
visited = [list(0 for _ in range(len(matrix))) for _ in range(len(matrix))]

total_ice = 0
group_ans = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        total_ice += matrix[i][j]
        if(matrix[i][j] != 0 and visited[i][j] == 0):
            q.append((i, j))
            visited[i][j] = 1
            curr_group = bfs()
            group_ans = max(group_ans, curr_group)

print(total_ice)
print(group_ans)