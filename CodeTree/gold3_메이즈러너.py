# N, M, K = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# player = [list(map(int, input().split())) for _ in range(M)]
# exit = list(map(int, input().split()))

N, M, K = 5, 3, 2
matrix = [[0, 0, 0, 0, 1],
[9, 2, 2, 0, 0],
[0, 1, 0, 1, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0]]
player = [[1, 3],
[3, 1],
[3, 5]]
exit = [3, 3]

print(matrix)
print(player)
print(exit)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동
player_move = []  # 플레이어가 이동할 수 있는 위치를 저장
answer_move = 0   # 플레이어의 이동 거리 합

for i in range(len(player)):
    matrix[player[i][0]-1][player[i][1]-1] = -1     # 사람이 있는걸 표시
    matrix[exit[0]-1][exit[1]-1] = -2   # 출구 표시

# 최단 거리 계산
def get_min_length(x1, y1, x2, y2):
    min_l = abs(x1 - x2) + abs(y1 - y2)
    return min_l


# 이동가능한 곳인지 판별하는 함수
def can_move(x, y):
    if (x <= 0 or y <= 0 or x > N or y > N):
        return False
    else:
        if (matrix[x - 1][y - 1] != 0):
            return False
        else:
            return True

# 이동함수
def move(n, x, y, answer_move):
    tmp = []
    exit_x, exit_y = exit  # 출구의 x, y 좌표
    min_len = get_min_length(x, y, exit_x, exit_y)  # 현재 플레이어 위치와 출구까지의 최단거리

    # 상하좌우 벽 확인 -> 벽이 없는 칸만 골라놓기
    for i in range(4):
        d_x, d_y = d[i]
        move_x, move_y = x + d_x, y + d_y  # 이동하게 되는 위치
        if (can_move(move_x, move_y)):
            tmp.append([move_x, move_y])

    # 현재 최단거리와 이동 후의 최단거리 비교 -> 이동 가능한 곳인지 판별
    for i in range(len(tmp)):
        if (i < len(tmp)):
            min_length_after_move = get_min_length(tmp[i][0], tmp[i][1], exit_x, exit_y)
            if (min_len > min_length_after_move):  # 최단거리가 아닌 위치라면 삭제
                player_move.append(tmp[i])

    # 벽으로 이동 불가하다면 리스트에 아무것도 남지 않음
    if (len(player_move) == 0):
        return

    # 이동 가능한 위치가 2개 이상이면 -> 상하 판단
    if (len(player_move) >= 2):
        get_x = abs(x - player_move[0][0])
        get_loc = player_move[0]
        for i in range(len(player_move)):
            new_x = abs(x - player_move[i][0])
            if (get_x < new_x):
                get_x = new_x
                get_loc = player_move[i]
        player[n] = get_loc
        answer_move += 1
        return

    elif (len(player_move) == 1):
        answer_move += 1
        player[n] = player_move
        return


def find_square(n):
    # n = 만들 정사각형 크기 (n * n)
    square_indices = []  # n * n 정사각형 배열 인덱스를 저장할 리스트

    for i in range(N - n + 1):
        for j in range(N - n + 1):
            # n*n 크기의 정사각형 배열 인덱스를 생성
            square = []
            for row in range(n):
                for col in range(n):
                    square.append([i + row + 1, j + col + 1])
            square_indices.append(square)

    return square_indices


square_selected = []
n_list = []  # 선택되는 사각형들의 한 변의 길이를 담을 리스트


# 플레이어 + 출구를 포함하는 n*n 정사각형 선택
def select_square(player_list, exit_list):
    square_list = []
    for n in range(2, N + 1):
        square_list = find_square(n)
        # 찾은 정사각형이 (플레이어 최소 1명 + 출구)를 포함하지 않으면 탈락 -> 포함하는 것들만 넣어두기
        for i in range(len(square_list)):
            for p in range(len(player_list)):
                if (player_list[p] in square_list[i] and exit_list in square_list[i]):
                    square_selected.append(square_list[i])
                    n_list.append(n)


# 시계방향 90도 회전
def square_rotate(index_list, length):
    # n*n 정사각형이므로 n개씩 쪼개서 한변으로 담아두기
    new_index_list = []
    for i in range((len(index_list) + length - 1) // length):
        start = i * length
        end = (i + 1) * length
        sublist = index_list[start:end]
        new_index_list.append(sublist)
    # [[[1, 1], [1, 2], [1, 3]],
    # [[2, 1], [2, 2], [2, 3]],
    # [[3, 1], [3, 2], [3, 3]]]

    rotated = []  # 90도 돌려진 인덱스 담기
    for i in range(len(new_index_list)):  # i = 0 1 2
        for j in range(len(new_index_list[i]) - 1, -1, -1):  # j = 2 1 0
            rotated.append(new_index_list[j][i])  # 20 10 00 ...

    unrotated = index_list
    return unrotated, rotated


# 전체 지도 변화
def matrix_rotate(index_list, rotate_list):
    # [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
    # [[3, 1], [2, 1], [1, 1], [3, 2], [2, 2], [1, 2], [3, 3], [2, 3], [1, 3]]

    # matrix 변화시키기
    after_rotate_value = []
    for i in range(len(rotate_list)):
        if(matrix[rotate_list[i][0] - 1][rotate_list[i][1] - 1] > 0):
            after_rotate_value.append(matrix[rotate_list[i][0] - 1][rotate_list[i][1] - 1] - 1)
        else:
            after_rotate_value.append(matrix[rotate_list[i][0] - 1][rotate_list[i][1] - 1])
            if (matrix[rotate_list[i][0] - 1][rotate_list[i][1] - 1] == -1):  # 사람이라면
                # player 이동시키기
                player_num = player.index([rotate_list[i][0], rotate_list[i][1]])
                player[player_num] = [index_list[i][0], index_list[i][1]]
            elif (matrix[rotate_list[i][0] - 1][rotate_list[i][1] - 1] == -2):  # 출구라면
                # 출구 위치 변경
                exit = [index_list[i][0], index_list[i][1]]

    # matrix 값 업데이트
    for i in range(len(rotate_list)):
        before_x, before_y = index_list[i][0] - 1, index_list[i][1] - 1
        matrix[before_x][before_y] = after_rotate_value[i]


for _ in range(K):
    for p in range(M):
        player_x, player_y = player[p][0], player[p][1]
        move(p, player_x, player_y, answer_move)

        all_out = True
        for i in range(len(player)):
            if(player[i] != exit):
                all_out = False
        if(all_out):
            break

    # 모든 플레이어 이동 후
    select_square(player, exit)  # 정사각형 선택
    rotated_x, rotate_o = square_rotate(square_selected[0], n_list[0])  # r과 c가 가장 작은 정사각형 -> 회전시키고 인덱스 번호들을 담은 배열
    matrix_rotate(rotated_x, rotate_o)

    # print(matrix)
    # print("===")

print(answer_move)
print(*exit)