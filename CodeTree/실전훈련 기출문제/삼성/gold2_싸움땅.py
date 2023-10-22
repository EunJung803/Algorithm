### 테케 4번
# n, m, k = 3, 5, 1
# matrix = [[0, 5, 0],
# [0, 0, 4],
# [5, 3, 0]]
# player = [[1, 1, 0, 2],
# [3, 3, 2, 1],
# [1, 3, 2, 5],
# [2, 1, 1, 3],
# [2, 2, 1, 4]]

### 테케 6번
# n, m, k = 5, 4, 6
# matrix = [[1, 2, 0, 1, 2],
# [1, 0, 3, 3, 1],
# [1, 3, 0, 2, 3],
# [2, 1, 2, 4, 5],
# [0, 1, 3, 2, 0]]
# player = [[1, 3, 2, 3], [2, 2, 1, 5], [3, 3, 2, 2], [5, 1, 3, 4]]

n, m, k = map(int, input().split())     # 공백 두고 input받기
matrix = [list(map(int, input().split())) for _ in range(n)]    # n * n 배열 입력받기
player = [list(map(int, input().split())) for _ in range(m)]    # 플레이어 2차원 배열로 입력받기

# matrix 맵의 각 요소를 배열로 바꾸기 (총을 떨어뜨렸을 때 바닥에 여러개의 총이 존재할 경우를 위해)
for i in range(n):
    for j in range(n):
        matrix[i][j] = [matrix[i][j]]

position = []       # 플레이어 현재 위치 [x, y]
player_s = []       # 플레이어 능력치
player_gun = []     # 플레이어가 소지한 총
player_d = []       # 플레이어 방향

answer = [0 for _ in range(m)]  # 각 플레이어가 획득할 포인트를 저장할 배열
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]    # 상 우 하 좌

# 플레이어 별 값 저장
for i in range(m):
    position.append([player[i][0]-1, player[i][1]-1])
    player_d.append(direction[player[i][2]])
    player_s.append(player[i][3])
    player_gun.append(0)

# 범위를 벗어나는지 확인하는 함수
def out_range(nx, ny):
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return True
    else:
        return False

# 이동 함수
def move(i, nx, ny):
    position[i] = [nx, ny]

# loser 이동 함수
def loser_move(i):
    x, y = position[i]      # 진 사람 위치
    dx, dy = player_d[i]    # 진 사람 방향값

    # 진 사람은 총을 버리고 이동해야 하므로 총 버리기
    if (player_gun[i] > 0):  # 총이 있는 경우
        matrix[x][y].append(player_gun[i])
        player_gun[i] = 0

    # 움직일 방향
    di = direction.index([dx, dy])
    # 90도씩 회전하며 갈 수 있는 곳 찾기
    while True:
        dx, dy = direction[di]
        nx, ny = x + dx, y + dy     # 이동할 위치
        check_range = out_range(nx, ny)
        # 격자 밖이거나 사람이 있으면 90도씩 회전
        if (check_range == True or ([nx, ny] in position)):
            di = (di+1) % 4
        else:
            player_d[i] = [dx, dy]
            break
    # 이동 후 떨어져있는 총을 들지말지 판별
    move(i, nx, ny)
    find_gun(i)

# 총을 주울지 말지 판별하고 액션하는 함수
def find_gun(i):
    nx, ny = position[i]            # 이동할 위치
    max_g = max(matrix[nx][ny])     # 바닥에 떨어진 총 중 가장 큰 공격력의 총
    # 플레이어 총없는 경우
    if player_gun[i] == 0:
        player_gun[i] = max_g
        matrix[nx][ny].remove(max_g)    # 가져간 총 바닥에서 지우기
        if not matrix[nx][ny]:          # 바닥에 아무것도 없으면 0으로 채우기
            matrix[nx][ny].append(0)
    else:
        # 플레이어가 바닥에 떨어진 총으로 가져가는 경우
        if player_gun[i] < max_g:
            matrix[nx][ny].remove(max_g)            # 플레이어가 총 가져가니까 바닥에서 지우기
            matrix[nx][ny].append(player_gun[i])    # 플레이어가 떨구는 총 맵에다가 추가
            if not matrix[nx][ny]:      # 바닥에 아무것도 없으면 0으로 채우기
                matrix[nx][ny].append(0)
            player_gun[i] = max_g       # 플레이어가 가져가는 총의 공격력으로 업데이트


def fight(i, j):
    player1_attack = player_s[i] + player_gun[i]    # 사람1의 공격력
    player2_attack = player_s[j] + player_gun[j]    # 사람2의 공격력

    # 공격력 비교
    if player1_attack > player2_attack:
        winner = i
        loser = j
    elif player1_attack < player2_attack:
        winner = j
        loser = i
    # 공격력이 같은 경우 -> 기본능력치로 비교
    else:
        if player_s[i] > player_s[j]:
            winner = i
            loser = j
        elif player_s[i] < player_s[j]:
            winner = j
            loser = i
        # 비기는 경우
        else:
            winner = 0
            loser = 0

    score = abs(player1_attack - player2_attack)
    answer[winner] += score

    return winner, loser


for _ in range(k):
    for i in range(m):
        # i == 플레이어 번호
        x, y = position[i]          # 현재 위치 인덱스
        dx, dy = player_d[i]        # 이동 거리로 더해줄 x,y의 방향값
        nx, ny = x + dx, y + dy     # 이동 후의 위치 인덱스

        # 범위 밖이라면 -> 뒤돌아서 이동
        if (out_range(nx, ny)):
            player_d[i] = [-player_d[i][0], -player_d[i][1]]
            dx, dy = player_d[i]
            nx, ny = x + dx, y + dy     # 이동 후의 위치 인덱스 업데이트

        ## 플레이어가 없다면
        if ([nx, ny] not in position):
            move(i, nx, ny)
            find_gun(i)
        ## 플레이어가 있다면
        else:
            j = position.index([nx, ny])    # 만나게 되는 플레이어 번호
            move(i, nx, ny)         # 상대방 있는 곳으로 이동
            winner, loser = fight(i, j)     # loser, winner 판별
            loser_move(loser)   # loser 이동 -> gun 판단
            find_gun(winner)    # winner -> gun 판단

print(*answer)
