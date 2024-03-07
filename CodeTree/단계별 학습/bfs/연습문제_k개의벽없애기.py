from collections import deque
from itertools import combinations

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
start, end = [list(map(int, input().split())) for _ in range(2)]

visited = [list(0 for _ in range(n)) for _ in range(n)]

ans = []
time_list = []

q = deque()

# 벽이 존재하는 좌표를 모두 wall_list에 추가해두기
wall_list = []
for i in range(n):
    for j in range(n):
        if(matrix[i][j] == 1):
            wall_list.append([i, j])

# combinations으로 제거할 벽의 조합 구하기
remove_wall = list(combinations(wall_list, k))

# 이동할 수 있는지 판별
def can_go(x, y, cp_matrix, visited):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    if(visited[x][y] == 1 or cp_matrix[x][y] == 1):
        return False
    else:
        return True

# 2차원 배열 복사 함수
def copy_matrix(m):
    new_m = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(m[i][j])
        new_m.append(tmp)
    return new_m

# BFS 탐색
def bfs(q, sub_matrix, visited):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    move_list = []

    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        cnt = curr[2]
        move_list.append((x, y, cnt))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(can_go(nx, ny, sub_matrix, visited)):
                visited[nx][ny] = 1
                q.append((nx, ny, cnt+1))

    return move_list

# 제거할 벽 좌표의 조합에서 하나씩 뽑아서 -> 원본 matrix를 복사해둔 sub_matrix에서 벽 제거
for i in range(len(remove_wall)):
    sub_matrix = copy_matrix(matrix)
    visited = [list(0 for _ in range(n)) for _ in range(n)]
    selected_wall = remove_wall[i]
    move_list = []

    for j in range(len(selected_wall)):
        remove_x = selected_wall[j][0]
        remove_y = selected_wall[j][1]
        sub_matrix[remove_x][remove_y] = 0

    # sub_matirx로 BFS 수행
    q.append((start[0]-1, start[1]-1, 0))
    visited[start[0]-1][start[1]-1] = 1
    move_list = bfs(q, sub_matrix, visited)

    # 도착 지점 좌표가 이동한 리스트에 존재한다면 -> 해당 거리 저장
    for m in range(len(move_list)):
        if(move_list[m][0] == end[0]-1 and move_list[m][1] == end[1]-1):
            ans.append(move_list)
            time_list.append(move_list[m][2])

            # for a in range(n):
            #     print(sub_matrix[a])
            # print("===")

            break

# print(ans)

# 도착 지점까지 이동할 수 있는 것 중 최소 거리 정답 출력
if(time_list):
    print(min(time_list))
else:   # 없으면 -1 출력
    print(-1)