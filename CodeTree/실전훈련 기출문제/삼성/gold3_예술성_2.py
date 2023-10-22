import sys
input = sys.stdin.readline

# 상하좌우
dxs, dys = [-1,1,0,0], [0,0,-1,1]

# n = int(input())
# board = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

n = 5
board = [[1, 2, 2, 3, 3], [2, 2, 2, 3, 3], [2, 2, 1, 3, 1], [2, 2, 1, 1, 1], [2, 2, 1, 1, 1]]

next_board = [
    [0]*n
    for _ in range(n)
]

visited = [
    [False]*n
    for _ in range(n)
] # 방문했는지 여부

group = [
    [0]*n
    for _ in range(n)
] # 몇번째 그룹인지
group_cnt = [0] * (n*n + 1)
group_n = 0 # 그룹 개수

def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 같은 그룹으로 묶기
def dfs(x, y):
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        if in_range(nx,ny) and not visited[nx][ny] and board[nx][ny] == board[x][y]:
            visited[nx][ny] = True
            group[nx][ny] = group_n
            group_cnt[group_n] += 1
            dfs(nx, ny)

# 그룹 만들기 (group에 각 그룹 정보 넣기, group_cnt에 각 그룹별 개수 정보)
def make_group():
    global group_n
    group_n = 0 # 초기화

    for i in range(n):
        for j in range(n):
            visited[i][j] = False # 그룹 방문 초기화

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                visited[i][j] = True
                group[i][j] = group_n
                group_cnt[group_n] = 1
                dfs(i, j)

# 점수 구하기 (각각 돌면서, 상하좌우로 서로 다른 그룹이라면, (해당 그룹의 칸수+상대그룹의 칸수)*그룹의값*상대그룹값*1
def get_score():
    make_group()

    score = 0

    for x in range(n):
        for y in range(n):
            for dx, dy in zip(dxs, dys):
                nx, ny = x+dx, y+dy
                if in_range(nx, ny) and board[x][y] != board[nx][ny]:
                    group_a, group_b = group[x][y], group[nx][ny]
                    count_a, count_b = group_cnt[group_a], group_cnt[group_b]
                    score += (count_a + count_b) * board[x][y] * board[nx][ny]

    return score // 2 # 중복 되는 값 제거


# 십자가 기준 4개의 정사각형 시계방향으로 회전 (가장 왼쪽 위 좌표: (sx,sy))
def rotate_square(sx, sy, length):
    for x in range(sx, sx + length):
        for y in range(sy, sy + length):
            ox, oy = x - sx, y - sy # (0,0) 으로 옮기기
            rx, ry = oy, length - ox - 1 # 시계 방향으로 회전
            next_board[rx + sx][ry + sy] = board[x][y] # 회전 후
def rotate():
    for i in range(n):
        for j in range(n):
            next_board[i][j] = 0

    length = n // 2
    # 십자가는 반시계 방향으로 돌리기
    # 세로 -> 가로 : (i,j) -> (j,i)
    # 가로 -> 세로: (i,j) -> (length-j-1, i)
    for i in range(n):
        for j in range(n):
            # 세로 -> 가로
            if j == length:
                next_board[j][i] = board[i][j]
            # 가로 -> 세로
            elif i == length:
                next_board[n - j - 1][i] = board[i][j]

    # 4개의 정사각형은 시계 방향으로 돌리기
    rotate_square(0, 0, length)
    rotate_square(0, length + 1, length)
    rotate_square(length + 1, 0, length)
    rotate_square(length + 1, length + 1, length)

    for i in range(n):
        for j in range(n):
            board[i][j] = next_board[i][j]

total_score = 0
# 3번 반복하기
for _ in range(4):
    total_score += get_score()
    rotate()

print(total_score)