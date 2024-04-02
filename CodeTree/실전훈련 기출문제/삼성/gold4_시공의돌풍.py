N, M, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 범위 확인 함수
def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= M):
        return False
    if(matrix[x][y] == -1):
        return False
    return True

# 먼지 카운트 함수
def count_all(matrix):
    result = 0
    for i in range(N):
        for j in range(M):
            if(matrix[i][j] != -1):
                result += matrix[i][j]
    return result

# 방향 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 먼지 확산 함수
def spread_dust():
    spread_idx = []
    for i in range(N):
        for j in range(M):
            if (matrix[i][j] != -1):

                spread = int(matrix[i][j] / 5)
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if (check_range(nx, ny)):
                        matrix[i][j] -= spread
                        spread_idx.append((spread, nx, ny))

    for s in spread_idx:
        matrix[s[1]][s[2]] += s[0]

# 돌풍의 위치 인덱스 담기
wind_idx = []
for i in range(N):
    for j in range(M):
        if (matrix[i][j] == -1):
            wind_idx.append((i, j))

def wind_move_up():
    # 돌풍의 윗칸 이동하기
    w1 = wind_idx[0]
    wx, wy = w1[0], w1[1]
    move_up = []
    tmpx, tmpy = 0, 0
    # →
    for i in range(1, M):
        nx, ny = wx, wy + i
        move_up.append((nx, ny))
        tmpx, tmpy = nx, ny
    # ↑
    for i in range(wx):
        nx, ny = tmpx-1, tmpy
        if(check_range(nx, ny)):
            tmpx, tmpy = nx, ny
            move_up.append((nx, ny))
    # ←
    for i in range(1, M):
        nx, ny = tmpx, tmpy-1
        if (check_range(nx, ny)):
            tmpx, tmpy = nx, ny
            move_up.append((nx, ny))
    # ↓
    for i in range(wx):
        nx, ny = tmpx+1, tmpy
        if (check_range(nx, ny)):
            tmpx, tmpy = nx, ny
            move_up.append((nx, ny))

    return move_up

def wind_move_down():
    # 돌풍의 아랫칸 이동하기
    w2 = wind_idx[1]
    wx, wy = w2[0], w2[1]
    move_down = []
    tmpx, tmpy = 0, 0
    # →
    for i in range(1, M):
        nx, ny = wx, wy + i
        move_down.append((nx, ny))
        tmpx, tmpy = nx, ny
    # ↓
    for i in range(wx, N):
        nx, ny = tmpx + 1, tmpy
        if(check_range(nx, ny)):
            tmpx, tmpy = nx, ny
            move_down.append((nx, ny))
    # ←
    for i in range(1, M):
        nx, ny = tmpx, tmpy - 1
        if (check_range(nx, ny)):
            tmpx, tmpy = nx, ny
            move_down.append((nx, ny))
    # ↑
    for i in range(N-1, wx+1, -1):
        nx, ny = tmpx - 1, tmpy
        if (check_range(nx, ny)):
            tmpx, tmpy = nx, ny
            move_down.append((nx, ny))

    return move_down


# 돌풍이 움직이는 위치 구하기
w_up = wind_move_up()       # 윗 부분
w_down = wind_move_down()   # 아랫 부분

cnt = 0

while(cnt < T):
    cnt += 1

    ## 먼지의 확산
    spread_dust()

    ## 시공의 돌풍 청소
    # 윗 부분 값 기억
    tmp_up = []
    for i in range(len(w_up)):
        x1, y1 = w_up[i][0], w_up[i][1]
        tmp_up.append(matrix[x1][y1])

    # 아랫 부분 값 기억
    tmp_down = []
    for i in range(len(w_down)):
        x2, y2 = w_down[i][0], w_down[i][1]
        tmp_down.append(matrix[x2][y2])

    # 돌풍이 불어서 0이 되는 곳
    matrix[wind_idx[0][0]][wind_idx[0][1] + 1] = 0
    matrix[wind_idx[1][0]][wind_idx[1][1] + 1] = 0

    # 윗부분 청소
    for i in range(len(w_up)-1):
        x, y = w_up[i+1][0], w_up[i+1][1]
        matrix[x][y] = tmp_up[i]

    # 아랫부분 청소
    for i in range(len(w_down)-1):
        x, y = w_down[i + 1][0], w_down[i + 1][1]
        matrix[x][y] = tmp_down[i]

# 정답 출력
print(count_all(matrix))