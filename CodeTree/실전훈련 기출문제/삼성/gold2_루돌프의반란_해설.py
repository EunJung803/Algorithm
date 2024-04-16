# # (x, y)가 보드 내의 좌표인지 확인하는 함수입니다.
# def is_inrange(x, y):
#     return 1 <= x and x <= n and 1 <= y and y <= n
#
# n, m, p, c, d = map(int, input().split())
# rudolf = tuple(map(int, input().split()))
#
# points = [0 for _ in range(p + 1)]
# pos = [(0, 0) for _ in range(p + 1)]
# board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# is_live = [False for _ in range(p + 1)]
# stun = [0 for _ in range(p + 1)]
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# board[rudolf[0]][rudolf[1]] = -1
#
# for _ in range(p):
#     id, x, y = tuple(map(int, input().split()))
#     pos[id] = (x, y)
#     board[pos[id][0]][pos[id][1]] = id
#     is_live[id] = True
#
# for t in range(1, m + 1):
#     closestX, closestY, closestIdx = 10000, 10000, 0
#
#     # 살아있는 포인트 중 루돌프에 가장 가까운 산타를 찾습니다.
#     for i in range(1, p + 1):
#         if not is_live[i]:
#             continue
#
#         currentBest = ((closestX - rudolf[0]) ** 2 + (closestY - rudolf[1]) ** 2, (-closestX, -closestY))
#         currentValue = ((pos[i][0] - rudolf[0]) ** 2 + (pos[i][1] - rudolf[1]) ** 2, (-pos[i][0], -pos[i][1]))
#
#         if currentValue < currentBest:
#             closestX, closestY = pos[i]
#             closestIdx = i
#
#     # 가장 가까운 산타의 방향으로 루돌프가 이동합니다.
#     if closestIdx:
#         prevRudolf = rudolf
#         moveX = 0
#         if closestX > rudolf[0]:
#             moveX = 1
#         elif closestX < rudolf[0]:
#             moveX = -1
#
#         moveY = 0
#         if closestY > rudolf[1]:
#             moveY = 1
#         elif closestY < rudolf[1]:
#             moveY = -1
#
#         rudolf = (rudolf[0] + moveX, rudolf[1] + moveY)
#         board[prevRudolf[0]][prevRudolf[1]] = 0
#
#     # 루돌프의 이동으로 충돌한 경우, 산타를 이동시키고 처리를 합니다.
#     if rudolf[0] == closestX and rudolf[1] == closestY:
#         firstX = closestX + moveX * c
#         firstY = closestY + moveY * c
#         lastX, lastY = firstX, firstY
#
#         stun[closestIdx] = t + 1
#
#         # 만약 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동이 일어납니다.
#         while is_inrange(lastX, lastY) and board[lastX][lastY] > 0:
#             lastX += moveX
#             lastY += moveY
#
#         # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
#         # 순차적으로 보드판에 있는 산타를 한칸씩 이동시킵니다.
#         while not (lastX == firstX and lastY == firstY):
#             beforeX = lastX - moveX
#             beforeY = lastY - moveY
#
#             if not is_inrange(beforeX, beforeY):
#                 break
#
#             idx = board[beforeX][beforeY]
#
#             if not is_inrange(lastX, lastY):
#                 is_live[idx] = False
#             else:
#                 board[lastX][lastY] = board[beforeX][beforeY]
#                 pos[idx] = (lastX, lastY)
#
#             lastX, lastY = beforeX, beforeY
#
#         points[closestIdx] += c
#         pos[closestIdx] = (firstX, firstY)
#         if is_inrange(firstX, firstY):
#             board[firstX][firstY] = closestIdx
#         else:
#             is_live[closestIdx] = False
#
#     board[rudolf[0]][rudolf[1]] = -1;
#
#     # 각 산타들은 루돌프와 가장 가까운 방향으로 한칸 이동합니다.
#     for i in range(1, p+1):
#         if not is_live[i] or stun[i] >= t:
#             continue
#
#         minDist = (pos[i][0] - rudolf[0])**2 + (pos[i][1] - rudolf[1])**2
#         moveDir = -1
#
#         for dir in range(4):
#             nx = pos[i][0] + dx[dir]
#             ny = pos[i][1] + dy[dir]
#
#             if not is_inrange(nx, ny) or board[nx][ny] > 0:
#                 continue
#
#             dist = (nx - rudolf[0])**2 + (ny - rudolf[1])**2
#             if dist < minDist:
#                 minDist = dist
#                 moveDir = dir
#
#         if moveDir != -1:
#             nx = pos[i][0] + dx[moveDir]
#             ny = pos[i][1] + dy[moveDir]
#
#             # 산타의 이동으로 충돌한 경우, 산타를 이동시키고 처리를 합니다.
#             if nx == rudolf[0] and ny == rudolf[1]:
#                 stun[i] = t + 1
#
#                 moveX = -dx[moveDir]
#                 moveY = -dy[moveDir]
#
#                 firstX = nx + moveX * d
#                 firstY = ny + moveY * d
#                 lastX, lastY = firstX, firstY
#
#                 if d == 1:
#                     points[i] += d
#                 else:
#                     # 만약 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동이 일어납니다.
#                     while is_inrange(lastX, lastY) and board[lastX][lastY] > 0:
#                         lastX += moveX
#                         lastY += moveY
#
#                     # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
#                     # 순차적으로 보드판에 있는 산타를 한칸씩 이동시킵니다.
#                     while lastX != firstX or lastY != firstY:
#                         beforeX = lastX - moveX
#                         beforeY = lastY - moveY
#
#                         if not is_inrange(beforeX, beforeY):
#                             break
#
#                         idx = board[beforeX][beforeY]
#
#                         if not is_inrange(lastX, lastY):
#                             is_live[idx] = False
#                         else:
#                             board[lastX][lastY] = board[beforeX][beforeY]
#                             pos[idx] = (lastX, lastY)
#
#                         lastX, lastY = beforeX, beforeY
#
#                     points[i] += d
#                     board[pos[i][0]][pos[i][1]] = 0
#                     pos[i] = (firstX, firstY)
#                     if is_inrange(firstX, firstY):
#                         board[firstX][firstY] = i
#                     else:
#                         is_live[i] = False
#             else:
#                 board[pos[i][0]][pos[i][1]] = 0
#                 pos[i] = (nx, ny)
#                 board[nx][ny] = i
#
#     # 라운드가 끝나고 탈락하지 않은 산타들의 점수를 1 증가시킵니다.
#     for i in range(1, p+1):
#         if is_live[i]:
#             points[i] += 1
#
#
# # 결과를 출력합니다.
# for i in range(1, p + 1):
#     print(points[i], end=" ")

import sys
import heapq

# sys.stdin=open('input.txt','r')
input = sys.stdin.readline

# 상우하좌
pdxs = [-1, 0, 1, 0]
pdys = [0, 1, 0, -1]


def in_range(nx, ny):
    return 0 < nx < N + 1 and 0 < ny < N + 1


def Distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2


# 상호작용
def Interaction(nx, ny, dx, dy):
    global all_in_board
    origin_player_id = board[nx][ny]
    origin_player_loc = playerIdToIndx[origin_player_id]
    opx, opy = origin_player_loc
    nx = opx + dx
    ny = opy + dy
    if not in_range(nx, ny):
        del playerIdToIndx[origin_player_id]  # 삭제
        all_in_board -= 1
        is_in_board[origin_player_id] = False
        return

    if board[nx][ny] > 0:  # 튕겨져나간 새 위치에 또 참가자가 있으면
        Interaction(nx, ny, dx, dy)

    board[nx][ny] = origin_player_id
    playerIdToIndx[origin_player_id] = [nx, ny]


# 충돌 2. 참가자가 소를 박음
def crush_player_to_cow(t, pid, dir):
    global board, cow_loc, players_score, all_in_board
    px, py = playerIdToIndx[pid]
    nx, ny = cow_loc
    players_score[pid] += D  # D만큼 점수를 얻음
    panic_time[pid] = t + 1
    dx = -pdxs[dir]  # 반대방향
    dy = -pdys[dir]

    nx = nx + dx * D
    ny = ny + dy * D
    if not in_range(nx, ny):  # 튕겨져 나간곳이 격자 밖이면
        board[px][py] = 0
        del playerIdToIndx[pid]  # 삭제
        all_in_board -= 1
        is_in_board[pid] = False
        return

    if board[nx][ny] > 0:  # 튕겨져 나간 곳에 사람이 있으면
        Interaction(nx, ny, dx, dy)

    # 아니면 튕겨져나간곳이 새로운 그사람 위치
    playerIdToIndx[pid] = [nx, ny]
    board[px][py] = 0
    board[nx][ny] = pid


# 참가자 움직임
def player_move(t, pid):
    global board, cow_loc

    cx, cy = cow_loc
    px, py = playerIdToIndx[pid]
    possible_loc = []
    cur_dis = Distance(px, py, cx, cy)
    for dir in range(4):
        nx = px + pdxs[dir]
        ny = py + pdys[dir]
        if in_range(nx, ny) and board[nx][ny] <= 0:
            dis = Distance(nx, ny, cx, cy)
            if dis < cur_dis:
                priority = [dis, dir, nx, ny]
                heapq.heappush(possible_loc, priority)

    if len(possible_loc) == 0:  # 4가지 경우 중 모두 없는 경우 끝냄
        return

    dis, dir, nx, ny = heapq.heappop(possible_loc)
    board[px][py] = 0
    if (nx, ny) == (cx, cy):  # 참가자가 소를 박음
        crush_player_to_cow(t, pid, dir)
    else:
        # 참가자가 소를 박은게 아니라면
        # 참가자 이동
        board[nx][ny] = pid
        playerIdToIndx[pid] = [nx, ny]


# 충돌 1. 소가 참가자를 박음  dir=[dirX,dirY]
def crush_cow_to_player(t, cx, cy, dir):
    global board, cow_loc, players_score, all_in_board
    pid = board[cx][cy]
    px, py = playerIdToIndx[pid]
    if playerIdToIndx[pid] != [cx, cy]:
        raise Exception('Error')
    players_score[pid] += C  # C만큼 점수를 얻음
    panic_time[pid] = t + 1
    px, py = playerIdToIndx[pid]
    nx, ny = px, py
    dx = dir[0]  # 반대방향
    dy = dir[1]

    nx = nx + dx * C
    ny = ny + dy * C
    if not in_range(nx, ny):  # 격자를 벗어남
        board[px][py] = 0  # 그 위치에 있던 사람은 없어지고
        del playerIdToIndx[pid]  # 삭제
        all_in_board -= 1
        is_in_board[pid] = False
        return

    if board[nx][ny] > 0:  # 튕겨져 나간 곳에 사람이 있으면
        Interaction(nx, ny, dx, dy)

    # 기존사람이 있든 없든 튕겨진 사람은 새로운 위치로
    playerIdToIndx[pid] = [nx, ny]
    board[px][py] = 0  # 기존 위치는 비우고
    board[nx][ny] = pid


# 소 움직임
def cow_move(t):
    global board, cow_loc
    cx, cy = cow_loc

    # 가장 가까운 참가자부터 찾는다.
    Finalx, Finaly, FinalId = 10000, 10000, 0
    for pid in range(1, P + 1):
        if not is_in_board[pid]:
            continue

        if playerIdToIndx[pid] == None:  # PID 참가자가 없으면 다음 참가자
            continue
        px, py = playerIdToIndx[pid]
        # 거리, 행, 열 순으로 우선순위
        farest_dis = [Distance(cx, cy, Finalx, Finaly), [-Finalx, -Finaly]]
        PID_dis = [Distance(cx, cy, px, py), [-px, -py]]

        if PID_dis < farest_dis:
            Finalx, Finaly = playerIdToIndx[pid]
            FinalId = pid

    # 가장 가까운 산타의 방향으로 루돌프가 이동합니다.
    if FinalId:  # 위 for문에서 조건을 만족 안해서 FinalId가 0을 유지했다면 이 조건문 안들어감

        dirX = 0
        if Finalx > cx:  # 현재 소위치보다 가장 가까운 참가자의 위치의 행이 더 크면
            dirX = 1  # 소 행으로 1만큼 이동
        elif Finalx < cx:  # 현재 소 위치보다 더 위에 있으면
            dirX = -1  # 소 위로 이동

        dirY = 0
        if Finaly > cy:  # 소보다 오른쪽에 있으면 오른쪽으로 이동
            dirY = 1
        elif Finaly < cy:  # 소보다 왼쪽에 있으면 왼쪽으로 이동
            dirY = -1

        cow_loc = [cx + dirX, cy + dirY]  # 소 위치 새 위치로 업데이트
        board[cx][cy] = 0  # 기존 소 위치 비워 두기

        dir = [dirX, dirY]  # 방향

        nx, ny = cow_loc
        px, py = playerIdToIndx[FinalId]
        if (px, py) == (nx, ny) or board[nx][ny] != 0:  # 소의 새 위치에 사람이 있으면
            crush_cow_to_player(t, nx, ny, dir)

        # 참가자랑 박치기를 하든 안하든 소가 이동만 한다
        board[nx][ny] = -1
        cow_loc = [nx, ny]

    # 가장 가까운 참가자가 없거나 이동할 필요가 없으면 이동 안함


def simulation(t):
    cow_move(t)

    # 만약 P 명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료됩니다.
    if all_in_board == 0:
        return

    for pid in range(1, P + 1):
        if not is_in_board[pid]:  # pid가 격자위에 없으면 다음 참가자 확인하기
            continue
        if panic_time[pid] < t:
            player_move(t, pid)

        # 만약 P 명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료됩니다.
        if all_in_board == 0:
            return
    # 매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여합니다.
    for pid in playerIdToIndx:
        players_score[pid] += 1


if __name__ == "__main__":
    # N:게임격자, M: 게임턴수, P:산타개수, C:루돌프 힘, D: 산타의 힘
    N, M, P, C, D = map(int, input().split())
    cow_loc = list(map(int, input().split()))

    board = [[0] * (N + 1) for _ in range(N + 1)]
    board[cow_loc[0]][cow_loc[1]] = -1

    playerIdToIndx = {}  # 참가자수 다 확인하며 점수를 부여하지 않기 위해

    players_score = [0] * (P + 1)  # 참가자 점수
    all_in_board = P  # 격자위 참가자 수
    panic_time = [0] * (P + 1)  # 참가자당 기절 시간
    is_in_board = [False] * (P + 1)  # 참가자당 격자위에 있는지 유무

    for _ in range(1, P + 1):
        pid, x, y, = map(int, input().split())
        board[x][y] = pid
        playerIdToIndx[pid] = [x, y]
        is_in_board[pid] = True

    for t in range(1, M + 1):
        simulation(t)
        if all_in_board == 0:
            break

    print(*players_score[1:])