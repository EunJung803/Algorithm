import copy
import math

N, M, P, C, D = map(int, input().split())
rudolf = list(map(int, input().split()))
santa = [list(map(int, input().split())) for _ in range(P)]

d = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
d_s = [(-1,0), (0,1), (1,0), (0,-1)]

matrix = [list(0 for _ in range(N)) for _ in range(N)]
point = [0 for _ in range(P)]

# 입력받은 루돌프 인덱스 재조정
rudolf[0] -= 1
rudolf[1] -= 1

# 입력받은 산타 인덱스 재조정
tmp = [[] for _ in range(P)]
for i in range(P):
    tmp[santa[i][0]-1] = [santa[i][1]-1, santa[i][2]-1]
    # santa[i][0] -= 1
    # santa[i][1] -= 1
    # santa[i][2] -= 1
santa = copy.deepcopy(tmp)
print(santa)
# 루돌프의 현재 방향
rudolf_d = 0
# 산타의 현재 방향
santa_d = [0 for _ in range(P)]

# 기절한 산타
faint_santa = [0 for _ in range(P)]

def get_dist(x1, x2, y1, y2):
    return int(math.pow(abs(x1 - x2), 2) + math.pow(abs(y1 - y2), 2))

def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    return True

def closer(x, y, target_x, target_y):
    go_list = []
    for i in range(len(d)):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if (check_range(nx, ny)):
            dist = get_dist(nx, target_x, ny, target_y)
            go_list.append([dist, nx, ny, i])
    go_list.sort(key=lambda x: x[0])
    return go_list[0]

def closer_forSanta(x, y, target_x, target_y):
    go_list = []
    for i in range(len(d_s)):
        nx = x + d_s[i][0]
        ny = y + d_s[i][1]
        if (check_range(nx, ny)):
            dist = get_dist(nx, target_x, ny, target_y)
            go_list.append([dist, nx, ny, i])
    go_list.sort(key=lambda x: (x[0], x[3]))
    # print("루돌프와 가까워지고 싶은 list", go_list)

    to_move = 0
    for i in range(len(go_list)):
        if([go_list[i][1], go_list[i][2]] not in santa):
            to_move = i
            break

    return go_list[to_move]


# 루돌프 이동
def ru_move():
    global rudolf_d
    min_dist = int(1e9)
    min_dist_list = []
    for i in range(P):
        if(santa[i]):
            dist = get_dist(santa[i][0], rudolf[0], santa[i][1], rudolf[1])
            min_dist = min(min_dist, dist)
            if(dist == min_dist):
                min_dist_list.append(santa[i])

    # min_dist_list.sort(key=lambda x:x[1], reverse=True)
    min_dist_list.sort(key=lambda x:(x[0], x[1]), reverse=True)
    print("가까운 길이의 산타들", min_dist_list)

    picked_santa = min_dist_list[0]
    print("가장 가까운 산타",picked_santa)

    rudolf_go = closer(rudolf[0], rudolf[1], picked_santa[0], picked_santa[1])

    # x = rudolf[0]
    # y = rudolf[1]
    # rudolf_go_list = []
    # for i in range(len(d)):
    #     nx = x + d[i][0]
    #     ny = y + d[i][1]
    #     if(check_range(nx, ny)):
    #         dist = get_dist(nx, picked_santa[1], ny, picked_santa[2])
    #         rudolf_go_list.append([dist, nx, ny])
    #
    # rudolf_go_list.sort(key=lambda x:x[0])
    # print(rudolf_go_list)
    #
    # rudolf[0] = rudolf_go_list[0][1]
    # rudolf[1] = rudolf_go_list[0][2]

    rudolf[0] = rudolf_go[1]
    rudolf[1] = rudolf_go[2]

    rudolf_d = rudolf_go[3]

    print("루돌프 리스트",rudolf)
    print("루돌프 방향",rudolf_d)


def santa_move():
    for i in range(P):
        if(faint_santa[i] > 0 or len(santa[i]) == 0):
            continue
        santa_go = closer_forSanta(santa[i][0], santa[i][1], rudolf[0], rudolf[1])
        santa[i][0] = santa_go[1]
        santa[i][1] = santa_go[2]
        santa_d[i] = santa_go[3]


def meet_santa(s1, s2, tmp_d):
    # s1 = 원래 그 자리 있던 산타, s2 = 밀려온 산타)
    santa[s2] = [santa[s1][0], santa[s1][1]]
    # santa[s1] = [santa[s1][0] + d[tmp_d][0], santa[s1][1] + d[tmp_d][1]]
    tmp_santa = [santa[s1][0] + d[tmp_d][0], santa[s1][1] + d[tmp_d][1]]

    if(tmp_santa in santa):
        idx = santa.index(tmp_santa)
        meet_santa(idx, s1, tmp_d)
    else:
        santa[s1] = tmp_santa


############################################
for _ in range(M):
    print(_, "턴")

    for i in range(P):
        if(faint_santa[i] > 0):
            faint_santa[i] -= 1

    print("이번 턴 기절해서 못 움직이는 산타", faint_santa)

    cnt = 0
    for i in range(P):
        if(len(santa[i]) == 0):
            cnt += 1

    if(cnt == P):
        break

    ru_move()

    print("산타 이동 전 산타", santa)

    # 루돌프가 이동 -> 산타 만남 -> 충돌 발생
    for i in range(P):
        if(rudolf == santa[i]):
            point[i] += C

            x = santa[i][0]
            y = santa[i][1]
            nx = x + d[rudolf_d][0] * C
            ny = y + d[rudolf_d][1] * C

            # santa_d[i] = rudolf_d

            faint_santa[i] += 2

            # 격자 밖 -> 탈락
            if(check_range(nx, ny) == False):
                santa[i] = []
                faint_santa[i] = 0

            else:
                if ([nx, ny] not in santa):
                    santa[i] = [nx, ny]
                    continue

                # 산타를 만나면 -> 상호작용
                elif([nx ,ny] in santa):
                    idx = santa.index([nx, ny])
                    meet_santa(idx, i, rudolf_d)

                    # 상호작용 후 탈락 된 산타 처리
                    for j in range(len(santa)):
                        if(santa[j]):
                            if(check_range(santa[j][0], santa[j][1]) == False):
                                santa[j] = []
                                faint_santa[j] = 0

    print("루돌프 이동 -> 충돌 산타", santa)

    print("산타 방향 (산타이동전)", santa_d)

    santa_move()

    print("산타 이동 후 산타", santa)

    print("산타 방향 (산타이동후)", santa_d)

    # 산타 이동 -> 루돌프 만남 -> 충돌 발생
    for i in range(P):
        if(rudolf == santa[i]):
            point[i] += D

            x = santa[i][0]
            y = santa[i][1]
            nx = x + d_s[(santa_d[i] + 2) % 4][0] * D
            ny = y + d_s[(santa_d[i] + 2) % 4][1] * D

            santa_d[i] = (santa_d[i] + 2) % 4

            faint_santa[i] += 2

            # 격자 밖 -> 탈락
            if (check_range(nx, ny) == False):
                santa[i] = []
                faint_santa[i] = 0

            else:
                if ([nx, ny] not in santa):
                    santa[i] = [nx, ny]
                    continue

                # 산타를 만나면 -> 상호작용
                elif ([nx, ny] in santa):
                    idx = santa.index([nx, ny])
                    meet_santa(idx, i, santa_d[i])

                    # 상호작용 후 탈락 된 산타 처리
                    for j in range(len(santa)):
                        if (santa[j]):
                            if (check_range(santa[j][0], santa[j][1]) == False):
                                santa[j] = []
                                faint_santa[j] = 0

    print("산타 이동 -> 충돌 산타", santa)

    print("기절한 산타", faint_santa)

    # 살아남았으면 포인트 +1
    for i in range(P):
        if(santa[i]):
            point[i] += 1

    print(point)
    print("==")