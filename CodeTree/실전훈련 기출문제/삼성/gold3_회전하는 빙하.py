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

def rotate(x, y, rotate_len, direction):
    # 0 : 좌, 1 : 우, 2 : 상, 3 : 하
    for i in range(x, x+rotate_len):
        for j in range(y, y+rotate_len):
            nx = i + dx[direction] * rotate_len
            ny = j + dy[direction] * rotate_len
            new_matrix[nx][ny] = matrix[i][j]


for q in range(len(rotate_lev)):
    new_matrix = copy.deepcopy(matrix)      # new_matrix 생성

    curr_lev = rotate_lev[q]        # 현재 선택된 레벨
    to_select = 2 ** curr_lev       # 해당 레벨에 따른 선택되는 격자 길이
    to_rotate = 2 ** (curr_lev - 1)     # 잘라서 회전되는 사각형의 길이

    if(curr_lev != 0):  # 레벨 0에서는 회전 X
        for i in range(0, len(matrix), to_select):
            for j in range(0, len(matrix), to_select):
                rotate(i, j, to_rotate, 1)                          # 좌측 상단 -> 우측 상단 (오른쪽으로 이동)
                rotate(i, j + to_rotate, to_rotate, 3)              # 우측 상단 -> 우측 하단 (아래로 이동)
                rotate(i + to_rotate, j + to_rotate, to_rotate, 0)  # 우측 하단 -> 좌측 하단 (왼쪽으로 이동)
                rotate(i + to_rotate, j, to_rotate, 2)              # 좌측 하단 -> 좌측 상단 (위로 이동)

    # 회전 (틀린 버젼)
    """
    for i in range(0, len(matrix), to_select):
        for j in range(0, len(matrix), to_select):
            # 각 사각형 시작점 : (i, j)
            for x in range(to_select):
                for y in range(to_select):
                    new_matrix[i+x][j+y] = matrix[i+to_select-1-y][j+x]
    """

    # 회전한 배열로 원래 matrix 업데이트
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


# 모든 회전 이후 남아있는 빙하의 총 양과 가장 큰 얼음 군집의 크기 구하기
q = deque()
visited = [list(0 for _ in range(len(matrix))) for _ in range(len(matrix))]

total_ice = 0   # 빙하의 총 양
group_ans = 0   # 가장 큰 얼음 군집의 크기

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

"""
def rotate(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            ox = i - x
            oy = j - y

            nx = oy
            ny = n - ox - 1

            nx += x
            ny += y

            new_matrix[nx][ny] = matrix[i][j]


# def rotate_2(x, y, n):
#     for i in range(x, n+x):
#         for j in range(y, n+y):
#             ox = i-x
#             oy = j-y
#
#             nx = oy
#             ny = n - ox - 1
#
#             nx += x
#             ny += y
#
#             new_matrix[nx][ny] = matrix[i][j]


new_matrix = copy.deepcopy(matrix)

curr_lev = 1
to_select = 2 ** curr_lev
part_select = 2 ** (curr_lev - 1)

for i in range(0, len(matrix), to_select):
    for j in range(0, len(matrix), to_select):
        rotate(i, j, to_select)

for i in range(len(new_matrix)):
    print(new_matrix[i])
print("==")

##################################

matrix = copy.deepcopy(new_matrix)

curr_lev = 2
to_select = 2 ** curr_lev
part_select = 2 ** (curr_lev - 1)

all_square = []
for i in range(0, len(matrix), to_select):
    for j in range(0, len(matrix), to_select):
        # rotate_2(i, j, to_select, part_select)
        square = []
        # 시작점 == (i, j)

        # 각 부분 사각형의 4개의 시작점
        # i, j
        # i + part_select, j
        # i, j + part_select
        # i + part_select, j + part_select

        square.append((i, j))
        square.append((i + part_select, j))
        square.append((i, j + part_select))
        square.append((i + part_select, j + part_select))

        all_square.append(square)

print(all_square)

        # for nn in range(0, to_select, part_select):
        #     tmp = []
        #     for x in range(i + nn, i + part_select):
        #         for y in range(j + nn, j + part_select):
        #             tmp.append((x, y))
        #     square.append(tmp)
        # print(square)


for i in range(len(new_matrix)):
    print(new_matrix[i])

# for q in range(Q):
#     curr_lev = rotate_lev[q]
#     to_select = 2**curr_lev
#     part_select = 2**(curr_lev-1)
#
#     for i in range(0, len(matrix), to_select):
#         rotate(i, i, part_select)
#
#     for i in range(len(new_matrix)):
#         print(new_matrix[i])

"""