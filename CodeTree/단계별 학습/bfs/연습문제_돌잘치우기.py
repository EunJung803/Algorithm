from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
start_point = [list(map(int, input().split())) for _ in range(k)]

rock_list = []

ans = []

# 돌이 있는 위치의 [x, y] 를 rock_list에 모두 담아주기
for i in range(n):
    for j in range(n):
        if(matrix[i][j] == 1):
            rock_list.append([i, j])

pick_rock = list(combinations(rock_list, m))        # 돌이 있는 위치에서 제거할 m개의 돌을 뽑는 모든 조합 구해서 pick_rock 리스트에 담기
# print(pick_rock)

# 기존 matrix에 저장된 값을 복사해서 반환해주는 함수 (원본 matrix 배열을 변형시키지 않기 위함)
def copy_matrix(matrix):
    cp = []
    for i in range(len(matrix)):
        sub = []
        for j in range(len(matrix[i])):
            sub.append(matrix[i][j])
        cp.append(sub)
    return cp

# 갈 수 있는 곳인지 판별해주는 함수
def can_go(x, y, sub_matrix, visited):
    if (x < 0 or y < 0 or x >= n or y >= n):
        return False
    if (sub_matrix[x][y] == 1 or visited[x][y] == 1):
        return False
    else:
        return True

# BFS 수행을 위한 준비
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 돌 제거 조합에서 -> 하나씩 뽑으며 -> 따로 복사한 matrix에서 치워보기 -> bfs로 시작점들 이동시켜보기 -> 횟수 저장해서 담기
for r in range(len(pick_rock)):
    rock = pick_rock[r]
    cp_matrix = copy_matrix(matrix)     # matrix 복사해서 cp_matrix에 저장

    # 뽑힌 조합으로 해당 위치에 있는 돌 제거
    for j in range(len(rock)):
        remove_x = rock[j][0]
        remove_y = rock[j][1]
        cp_matrix[remove_x][remove_y] = 0

    # BFS 수행
    move = 0
    visited = [list(0 for _ in range(n)) for _ in range(n)]

    for p in range(len(start_point)):   # 각 시작점을 큐잉해서 탐색 !!!!!
        move += 1
        point = start_point[p]
        q.append([point[0]-1, point[1]-1, move])        # 큐에 각 시작점 값들을 하나씩 append
        visited[point[0]-1][point[1]-1] = 1

    while (q):  # BFS 탐색 시작
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if (can_go(new_x, new_y, cp_matrix, visited)):
                move += 1
                visited[new_x][new_y] = 1
                q.append([new_x, new_y, move])

    ans.append(move)

print(ans)
print(max(ans))

# all_matrix = []
# tmp = m
# moved = [list(0 for _ in range(n)) for _ in range(n)]

# # 돌의 총 개수 카운트
# rock = 0
# for i in range(n):
#     rock += matrix[i].count(1)
#
# print(rock)
#
# # matrix 저장된 값 복사해두기
# def copy_matrix(matrix):
#     cp = []
#     for i in range(len(matrix)):
#         sub = []
#         for j in range(len(matrix[i])):
#             sub.append(matrix[i][j])
#         cp.append(sub)
#     return cp
#
# for _ in range(rock // m):
#     moved_matrix = copy_matrix(matrix)
#
#     # 돌 m개를 치워보는 모든 경우
#     for i in range(n):
#         for j in range(n):
#             if(m > 0):
#                 if(moved_matrix[i][j] == 1 and moved[i][j] == 0):
#                     m -= 1
#                     moved_matrix[i][j] = 0
#                     moved[i][j] = 1
#             else:
#                 break
#     all_matrix.append(moved_matrix)
#     m = tmp
#
#
# print(all_matrix)
"""
ans = []
move = 1

moved_matrix = []
for i in range(len(matrix)):
    moved_matrix.append(matrix[i])

moved_m = m

def can_go(x, y):
    if (x < 0 or y < 0 or x >= n or y >= n):
        return False
    if (moved_matrix[x][y] == 1 or visited[x][y] == 1):
        return False
    else:
        return True

q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
"""
"""
for p in range(len(start_point)):
    point = start_point[p]
    q.append([point[0], point[1], move])

    while(q):
        print(q)
        curr = q.popleft()
        x = curr[0] - 1
        y = curr[1] - 1

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if (new_x >= 0 and new_y >= 0 and new_x < n and new_y < n):
                if (moved_matrix[new_x][new_y] == 1 and moved_m > 0):
                    moved_matrix[new_x][new_y] = 0
                    moved_m -= 1

            if(can_go(new_x, new_y)):
                move += 1
                visited[new_x][new_y] = 1
                q.append([new_x, new_y, move])

    ans.append(move)
    move = 1
    visited = [list(0 for _ in range(n)) for _ in range(n)]
    moved_matrix = []
    for i in range(len(matrix)):
        moved_matrix.append(matrix[i])
    moved_m = m

print(ans)
"""