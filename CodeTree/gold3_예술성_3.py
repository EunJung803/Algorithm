from collections import deque

n = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

group_cnt = 0
group = [[[]] * n for _ in range(n)]  # 그룹번호, 숫자값, 개수
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, num):
    global group_cnt

    q = deque()
    visited[x][y] = 1
    group_cnt += 1
    q.append((x, y))

    k = 0
    while k < len(q):
        px, py = q[k]
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if num == arr[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        k += 1

    for px, py in q:
        group[px][py] = [group_cnt, num, len(q)]


score = 0


def diff_count(x, y):
    global score
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    start_g = group[x][y][0]
    g = 0
    info = []
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if group[nx][ny][0] == start_g:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    diff[start_g][group[nx][ny][0]] += 1
                    info.append((nx, ny))

    group_visit = [0 for _ in range(group_cnt + 1)]
    for i in range(len(info)):
        nx, ny = info[i]
        if not group_visit[group[nx][ny][0]]:
            score += (group[x][y][2] + group[nx][ny][2]) * group[x][y][1] * group[nx][ny][1] * diff[group[x][y][0]][
                group[nx][ny][0]]
            group_visit[group[nx][ny][0]] = 1


def plus_rotate():  # 십자가 모양 반시계 방향 회전
    for i in range(n):
        for j in range(n):
            if i == half:
                temp_arr[i][j] = arr[j][i]
            if j == half:
                temp_arr[i][j] = arr[n - j - 1][n - i - 1]


def square_rotate(x, y, l):  # 정사각형 모양 시계 방향 회전
    for i in range(x, x + l):
        for j in range(y, y + l):
            ox, oy = i - x, j - y  # (0, 0)으로 변환
            rx, ry = oy, l - ox - 1  # 시계 방향 회전 공식
            temp_arr[rx + x][ry + y] = arr[i][j]  # 모든 좌표에 적용할 수 있도록 인자(x, y)를 더해줌.


half = n // 2
total_score = 0
for _ in range(4):
    # 초기화
    group_cnt = 0
    group = [[[]] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    score = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, arr[i][j])

    visited = [[0] * n for _ in range(n)]
    diff = [[0 for _ in range(group_cnt + 1)] for _ in range(group_cnt + 1)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                diff_count(i, j)

    total_score += score

    temp_arr = [[0] * n for _ in range(n)]
    plus_rotate()  # 십자가 회전

    # 부분 사각형 회전
    square_rotate(0, 0, half)
    square_rotate(0, half + 1, half)
    square_rotate(half + 1, 0, half)
    square_rotate(half + 1, half + 1, half)

    # 배열 업데이트
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp_arr[i][j]

print(total_score)

