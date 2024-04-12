N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
player = [list(map(int, input().split())) for _ in range(M)]    # (x, y), d, s

## 플레이어의 위치 인덱스 1씩 빼주고 시작
for i in range(M):
    player[i][0] -= 1
    player[i][1] -= 1

## 총 배열 생성
gun_matrix = [list([] for _ in range(N)) for _ in range(N)]
for i in range(N):
    for j in range(N):
        gun_matrix[i][j].append(matrix[i][j])

## 방향벡터 : 순서대로 ↑, →, ↓, ←
dx = [-1,0,1,0]
dy = [0,1,0,-1]

point = [0 for _ in range(M)]           # 각 플레이어 포인트
player_gun = [0 for _ in range(M)]      # 각 플레이어가 들고있는 총

## 각 플레이어의 현재 위치 저장
player_position = [[] for _ in range(M)]
for i in range(M):
    player_position[i] = [player[i][0], player[i][1]]

## 범위 확인 함수
def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    return True

## 총 획득 함수
def get_gun(x, y, num):
    floor_gun = max(gun_matrix[x][y])
    my_gun = player_gun[num]

    # 현재 플레이어가 들고있는 총이 없으면 -> 총 줍기
    if(my_gun == 0):
        player_gun[num] += floor_gun
        gun_matrix[x][y].remove(floor_gun)

    # 총 들고있는데 바닥에 있는 총이 더 센 총이면 -> 총 줍기
    else:
        if(my_gun < floor_gun):
            player_gun[num] -= my_gun       # 내려놓기
            player_gun[num] += floor_gun
            gun_matrix[x][y].remove(floor_gun)
            gun_matrix[x][y].append(my_gun)

    # 총 배열이 빈칸이면 0으로 채워주기
    if(len(gun_matrix[x][y]) == 0):
        gun_matrix[x][y].append(0)

## 진 사람 -> 총 내려놓고 한칸 움직이는 함수
def loser_move(num):
    x = player[num][0]
    y = player[num][1]
    d = player[num][2]
    s = player[num][3]

    # 총 내려놓기
    my_gun = player_gun[num]
    if (my_gun != 0):
        player_gun[num] -= my_gun
        gun_matrix[x][y].append(my_gun)

    nx = x + dx[d]
    ny = y + dy[d]

    # 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우
    if([nx, ny] in player_position or check_range(nx,ny) == False):
        while([nx, ny] in player_position or check_range(nx,ny) == False):
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if([nx, ny] not in player_position and check_range(nx,ny)):
                break

    # 이동한 칸의 총 줍기 판단, 플레이어 위치 업데이트
    get_gun(nx, ny, num)
    player[num] = [nx, ny, d, s]
    player_position[num] = [nx, ny]

## 싸움 함수
def fight(p1, p2):
    p1_power = player_gun[p1] + player[p1][3]
    p2_power = player_gun[p2] + player[p2][3]

    # 둘 중 공격력이 센 사람이 승리
    if(p1_power > p2_power):
        # 진 사람 이동
        loser_move(p2)
        # 이긴 사람은 바닥에 떨어진 총 줍기 판단
        winner_x, winner_y = player[p1][0], player[p1][1]
        get_gun(winner_x, winner_y, p1)
        # 이긴 사람은 포인트 얻기
        point[p1] += abs(p1_power - p2_power)
        return
    if (p1_power < p2_power):
        loser_move(p1)
        winner_x, winner_y = player[p2][0], player[p2][1]
        get_gun(winner_x, winner_y, p2)
        point[p2] += abs(p1_power - p2_power)
        return

    # 공격력이 같다면 -> 초기 능력치로 비교
    else:
        if(player[p1][3] > player[p2][3]):
            loser_move(p2)
            winner_x, winner_y = player[p1][0], player[p1][1]
            get_gun(winner_x, winner_y, p1)
            point[p1] += abs(p1_power - p2_power)
            return
        if(player[p1][3] < player[p2][3]):
            loser_move(p1)
            winner_x, winner_y = player[p2][0], player[p2][1]
            get_gun(winner_x, winner_y, p2)
            point[p2] += abs(p1_power - p2_power)
            return

## 플레이어 이동 함수
def move_player():
    for i in range(len(player)):
        x = player[i][0]
        y = player[i][1]
        d = player[i][2]
        s = player[i][3]

        nx = x + dx[d]
        ny = y + dy[d]

        if(check_range(nx, ny) == False):   # 격자 밖이면 방향 꺾기
            d = (d + 2) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        # 이동한 위치로 업데이트
        player[i] = [nx, ny, d, s]

        # 다른 플레이어 만남 -> 싸움
        if([nx, ny] in player_position):
            other_num = player_position.index([nx, ny])
            player_position[i] = [nx, ny]       # 위치 업데이트
            fight(i, other_num)

        # 안만남
        else:
            get_gun(nx, ny, i)
            player_position[i] = [nx, ny]       # 위치 업데이트


### Main 실행 ###
for _ in range(K):
    move_player()

print(*point)