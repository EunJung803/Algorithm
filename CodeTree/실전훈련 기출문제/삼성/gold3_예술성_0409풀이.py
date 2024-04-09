import copy
from collections import deque
from itertools import combinations

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

q = deque()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

## 범위를 체크하는 함수
def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    return True

## 인접한 동일한 숫자를 그룹으로 만드는 함수 (BFS)
def bfs():
    group_idx = []
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        g_num = curr[2]

        group_idx.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(check_range(nx, ny) and visited[nx][ny] == 0 and matrix[nx][ny] == g_num):
                visited[nx][ny] = 1
                q.append((nx, ny, g_num))

    return group_idx

## 예술 점수 계산 함수
def cal_art_score(g1_idx, g2_idx, wall):
    g1, g2 = all_groups[g1_idx], all_groups[g2_idx]
    g1_num, g2_num = matrix[g1[0][0]][g1[0][1]], matrix[g2[0][0]][g2[0][1]]

    score = (len(g1) + len(g2)) * g1_num * g2_num * wall

    return score


## 그룹 두개의 맞닿아 있는 변의 수를 구하는 함수
def meeting_wall(g1, g2):
    cnt = 0
    for i in range(len(g1)):
        x = g1[i][0]
        y = g1[i][1]
        for j in range(4):      # g1 그룹에서 상하좌우로 한칸씩 이동했을 때, g2 그룹에 있는 인덱스와 동일하면 -> 그 두 인덱스는 맞닿아있음
            nx = x + dx[j]
            ny = y + dy[j]
            if(check_range(nx, ny) and (nx, ny) in g2):
                cnt += 1
    return cnt

## 십자가 회전
def rotate_cross():
    for i in range(N):
        for j in range(N):
            if(i == N//2):  # 가로 부분
                x = N - j - 1
                y = i
                new_matrix[x][y] = matrix[i][j]
            if(j == N//2):  # 세로 부분
                x = j
                y = i
                new_matrix[x][y] = matrix[i][j]

## 부분 정사각형 회전
def rotate_square(x, y, n):
    # (x, y)가 정사각형의 시작점 (제일 왼쪽 상단 값)
    for i in range(x, x+n):
        for j in range(y, y+n):
            # (0, 0) 으로 변환
            ox = i - x
            oy = j - y

            # 정사각형 우측 90도 회전
            nx = oy
            ny = n - ox - 1

            # 다시 원래 인덱스로 복귀
            nx += x
            ny += y

            new_matrix[nx][ny] = matrix[i][j]


######## Main 실행
total_score = 0
new_matrix = copy.deepcopy(matrix)      # 초기 복사

for _ in range(4):
    visited = [list(0 for _ in range(N)) for _ in range(N)]

    # 그룹 만들기 -> 모든 그룹 all_groups에 넣어두기
    all_groups = []

    for i in range(N):
        for j in range(N):
            if(visited[i][j] == 0):
                q.append((i, j, matrix[i][j]))
                visited[i][j] = 1
                g_idx = bfs()
                all_groups.append(g_idx)

    # 그룹 쌍 간의 조화로움을 계산하기 위해 2개씩의 그룹을 뽑는 조합 생성
    tmp = [i for i in range(len(all_groups))]
    combi = list(combinations(tmp, 2))

    # 각 그룹 쌍의 맞닿은 변의 수 저장해두기
    wall_list = []
    for i in range(len(combi)):
        cnt = meeting_wall(all_groups[combi[i][0]], all_groups[combi[i][1]])
        wall_list.append((combi[i], cnt))

    # 예술 점수 계산
    for i in range(len(wall_list)):
        if(wall_list[i][1] == 0):
            continue
        else:
            g1_idx, g2_idx = wall_list[i][0][0], wall_list[i][0][1]
            total_score += cal_art_score(g1_idx, g2_idx, wall_list[i][1])

    # 십자가 회전
    rotate_cross()

    # 부분 정사각형 회전
    n = N//2
    # 좌측 상단 회전
    rotate_square(0, 0, n)
    # 좌측 하단 회전
    rotate_square(n+1, 0, n)
    # 우측 상단 회전
    rotate_square(0, n+1, n)
    # 우측 하단 회전
    rotate_square(n+1, n+1, n)

    # 회전된 배열로 업데이트
    matrix = copy.deepcopy(new_matrix)

print(total_score)