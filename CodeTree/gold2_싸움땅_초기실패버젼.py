n, m, k = 5, 4, 6
matrix = [[1, 2, 0, 1, 2],
[1, 0, 3, 3, 1],
[1, 3, 0, 2, 3],
[2, 1, 2, 4, 5],
[0, 1, 3, 2, 0]]
player = [[1, 3, 2, 3], [2, 2, 1, 5], [3, 3, 2, 2], [5, 1, 3, 4]]

answer = [0, 0, 0, 0]  # 각 플레이어가 획득할 포인트를 저장할 배열
player_move = [[0 for _ in range(n)] for _ in range(n)]     # 플레이어의 위치를 담을 2차 배열

player_dict = dict()    # [플레이어 번호] : [기본 능력치, 얻은 총의 공격력]
direc_dict = dict()     # [플레이어 번호] : [이동 방향 인덱스]

for i in range(m):
    player_dict[i + 1] = [player[i][3]]  # 능력치 배열에 넣어서 저장
    direc_dict[i + 1] = player[i][2]  # 각 플레이어의 이동 방향 저장
    player_move[player[i][0]-1][player[i][1]-1] = i+1       # 플레이어 위치 저장

# 이동 방향 (d값에 따른 상좌하우 xy 방향)
d_x = [-1, 0, 1, 0]
d_y = [0, 1, 0, -1]

for _ in range(k):
    for i in range(len(player)):
        # i + 1 == 플레이어 번호
        # 현재 플레이어 위치
        player_x = player[i][0] - 1
        player_y = player[i][1] - 1
        # 가야할 방향
        d = direc_dict[i + 1]

        # 범위 밖이라면 반대로
        if (player_x + d_x[d] >= n or player_y + d_y[d] >= n or player_x + d_x[d] < 0 or player_y + d_y[d] < 0):
            d = (d + 2) % 4
            direc_dict[i + 1] = d

        # 이동하려는 곳
        to_go = matrix[player_x + d_x[d]][player_y + d_y[d]]

        # 이동하려는 곳에 총이 있으면
        if (to_go >= 0 and player_move[player_x + d_x[d]][player_y + d_y[d]] == 0):
            if (len(player_dict[i + 1]) > 1):  # 플레이어가 총이 있다면 -> 비교해서 가져가기
                player_dict[i + 1][1] = max(player_dict[i + 1][1], to_go)
                matrix[player_x + d_x[d]][player_y + d_y[d]] = min(player_dict[i + 1][1], to_go)  # 가져가지 않는 총 내려놓기
            else:
                player_dict[i + 1].append(to_go)
                matrix[player_x + d_x[d]][player_y + d_y[d]] = 0
            # 이동
            player_move[player_x][player_y] = 0
            player_move[player_x + d_x[d]][player_y + d_y[d]] = i + 1
            # 이동 위치 저장
            player[i][0] = player_x + d_x[d] + 1
            player[i][1] = player_y + d_y[d] + 1
            continue

        # 이동하려는 곳에 사람이 있으면
        if (player_move[player_x + d_x[d]][player_y + d_y[d]] != 0):
            # 공격력 비교로 싸우기
            standing = player_move[player_x + d_x[d]][player_y + d_y[d]]
            move_check = True   # 이동하려는 사람이 이기면 True, 아니면 False
            ## 1. 이동하려는 사람 WIN > 서있는 사람 LOSE
            if (sum(player_dict[i + 1]) > sum(player_dict[standing])):
                answer[i] = sum(player_dict[i + 1]) - sum(player_dict[standing])
                loser_num = standing
                winner_num = i + 1
                loser = player_dict[standing]
                winner = player_dict[i + 1]

            ## 2. 이동하려는 사람 LOSE < 서있는 사람 WIN
            elif (sum(player_dict[i + 1]) < sum(player_dict[standing])):
                answer[standing - 1] = sum(player_dict[standing]) - sum(player_dict[i + 1])
                loser_num = i + 1
                winner_num = standing
                loser = player_dict[i + 1]
                winner = player_dict[standing]
                move_check = False

            ## 3. 같은 공격력 -> 기본 능력치로 비교
            else:
                if (player_dict[i + 1][0] > player_dict[standing][0]):
                    answer[i] = sum(player_dict[i + 1]) - sum(player_dict[standing])
                    loser_num = standing
                    winner_num = i + 1
                    loser = player_dict[standing]
                    winner = player_dict[i + 1]
                else:
                    answer[standing - 1] = sum(player_dict[standing]) - sum(player_dict[i + 1])
                    loser_num = i + 1
                    winner_num = standing
                    loser = player_dict[i + 1]
                    winner = player_dict[standing]
                    move_check = False

            ### 진 사람과 이긴 사람 이동 처리
            # 이긴 사람 위치 이동 or not 결정
            loser_d = direc_dict[loser_num]
            if(move_check == True):     # 이동하는 사람이 이김
                # 진 사람 원래 위치 (서있던 사람)
                loser_x = player[loser_num - 1][0] - 1
                loser_y = player[loser_num - 1][1] - 1
                # 이긴 사람 이동
                player_move[player_x][player_y] = 0
                player_move[player_x + d_x[d]][player_y + d_y[d]] = winner_num
                # 이동 위치 저장
                player[winner_num-1][0] = player_x + d_x[d] + 1
                player[winner_num-1][1] = player_y + d_y[d] + 1
                # 진 사람 -> 총 내려놓고 -> 원래 방향 이동
                if (len(loser) > 1):
                    matrix[player_x + d_x[d]][player_y + d_y[d]] = max(to_go, loser.pop(1))
                d = loser_d

            if(move_check == False):    # 이동하는 사람이 짐
                # 진 사람 원래 위치 (이동하려는 사람)
                loser_x = player[loser_num - 1][0] - 1
                loser_y = player[loser_num - 1][1] - 1
                # 진 사람 -> 총 내려놓고 -> 원래 방향 이동
                if (len(loser) > 1):
                    matrix[player_x + d_x[d]][player_y + d_y[d]] = max(to_go, loser.pop(1))

            for a in range(4):
                loser_d = (loser_d + a) % 4
                if ((0 <= loser_x + d_x[loser_d] < n) and (0 <= loser_y + d_y[loser_d] < n)):
                    if(player_move[player_x + d_x[loser_d]][player_y + d_y[loser_d]] == 0):
                        break

            direc_dict[loser_num] = loser_d
            player_move[loser_x][loser_y] = 0
            player_move[player_x + d_x[d] + d_x[loser_d]][player_y + d_y[d] + d_y[loser_d]] = loser_num
            # 진 사람 이동 위치 저장
            player[loser_num - 1][0] = player_x + d_x[d] + d_x[loser_d] + 1
            player[loser_num - 1][1] = player_y + d_y[d] + d_y[loser_d] + 1

            # 이동한 곳에 총이 있으면 비교해서 가져가기
            if (matrix[player_x + d_x[d] + d_x[loser_d]][player_y + d_y[d] + d_y[loser_d]] > 0):
                if (len(loser) > 1):  # 플레이어가 총이 있다면 -> 비교해서 가져가기
                    player_dict[loser_num][1] = max(player_dict[loser_num][1], matrix[player_x + d_x[d] + d_x[loser_d]][player_y + d_y[d] + d_y[loser_d]])
                else:
                    loser.append(matrix[player_x + d_x[d] + d_x[loser_d]][player_y + d_y[d] + d_y[loser_d]])
                    matrix[player_x + d_x[d] + d_x[loser_d]][player_y + d_y[d] + d_y[loser_d]] = 0

            # 이긴 사람 -> 총 가져갈지 말지
            player_dict[winner_num][1] = max(player_dict[winner_num][1], to_go)


print(*answer)