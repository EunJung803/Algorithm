# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]

n = 5
matrix = [[1, 2, 2, 3, 3], [2, 2, 2, 3, 3], [2, 2, 1, 3, 1], [2, 2, 1, 1, 1], [2, 2, 1, 1, 1]]

# 6번 테케
# n = 15
# matrix = [
#     [1, 10, 2, 4, 4, 1, 10, 10, 7, 7, 3, 4, 4, 1, 4],
#     [2, 7, 4, 4, 9, 4, 2, 2, 1, 10, 10, 2, 7, 2, 2],
#     [10, 9, 3, 9, 2, 7, 10, 10, 10, 7, 9, 9, 9, 9, 1],
#     [4, 10, 2, 1, 3, 10, 1, 9, 10, 4, 4, 10, 7, 7, 10],
#     [4, 2, 1, 10, 4, 3, 10, 1, 9, 1, 7, 1, 1, 3, 1],
#     [4, 10, 7, 2, 3, 9, 7, 4, 10, 10, 10, 1, 4, 7, 7],
#     [2, 2, 1, 7, 10, 7, 4, 1, 1, 3, 3, 1, 9, 1, 2],
#     [3, 2, 2, 2, 9, 10, 2, 9, 3, 1, 1, 1, 10, 2, 9],
#     [1, 4, 2, 3, 1, 3, 1, 10, 9, 7, 9, 7, 2, 9, 4],
#     [4, 10, 2, 10, 4, 2, 9, 10, 3, 4, 7, 4, 7, 4, 1],
#     [1, 1, 9, 4, 7, 3, 7, 3, 1, 10, 1, 10, 2, 4, 1],
#     [4, 10, 4, 2, 9, 1, 3, 3, 3, 3, 1, 4, 10, 1, 3],
#     [3, 2, 4, 10, 2, 2, 2, 10, 9, 3, 4, 9, 3, 2, 7],
#     [2, 1, 7, 1, 3, 3, 2, 10, 9, 1, 7, 3, 1, 2, 4],
#     [7, 10, 7, 3, 2, 1, 3, 2, 1, 4, 3, 3, 10, 9, 10]
# ]

check_visit = [[0 for i in range(n)] for j in range(n)]

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 좌상우하
group = []

answer = 0

sn = n // 2     # 선택되는 정사각형의 한 변


## 범위를 벗어나는지 판단하는 함수
def check_range(x, y):
    if (x < 0 or y < 0 or x >= n or y >= n):
        return False
    else:
        return True


## 그룹 만들기
def make_group(i, j):
    start = matrix[i][j]  # 초기값
    check_visit[i][j] = 1
    sub_arr = [(i, j)]  # 만들어지는 그룹을 저장할 배열
    arr = [(i, j)]  # 상하좌우를 탐색해야할 인덱스
    while (arr):
        i, j = arr.pop(0)
        for l in range(len(d)):  # 상하좌우에 같은게 있는지 보기
            dx, dy = d[l][0], d[l][1]
            x, y = i + dx, j + dy

            if (check_range(x, y)):
                if (check_visit[x][y] == 0):
                    if (matrix[x][y] == start and (x, y) not in sub_arr):  # 같은거 있으면 그룹에 추가
                        sub_arr.append((x, y))
                        arr.append((x, y))
                        start = matrix[x][y]
                        check_visit[x][y] = 1

    # 이미 그룹화 되어있는 애면 최종 그룹에 추가하지 않음
    for i in range(len(sub_arr)):
        for j in range(len(group)):
            if (sub_arr[i] in group[j]):
                return

    group.append(sub_arr)


## 맞닿은 변의 개수 구하는 함수
def get_meeting_wall(group1, group2):
    result = 0

    for i in range(len(group1)):
        row, col = group1[i][0], group1[i][1]
        for l in range(len(d)):
            dx, dy = d[l][0], d[l][1]
            x, y = row + dx, col + dy
            if (check_range(x, y)):
                if ((x, y) in group2):
                    result += 1
    return result


## 조화로움 점수 계산하는 함수
def cal_point(group1, group2, group1_num, group2_num, meeting_wall):
    return (len(group1) + len(group2)) * group1_num * group2_num * meeting_wall


## 십자가 선택하고 회전
def select_cross_rotate():
    # 십자가 인덱스 담기
    arr = []
    for i in range(n):
        if (i != n // 2):
            arr.append((i, n // 2))
            arr.append((n // 2, i))
    cross = sorted(list(set(arr)))

    # 회전하기
    rotate_corss = []
    for i in range(0, len(cross), 2):
        if (i + 1 > len(cross)):
            break
        x1, y1 = cross[i][0], cross[i][1]
        x2, y2 = cross[i + 1][0], cross[i + 1][1]

        if (y1 == y2):  # 세로 -> 가로
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        elif (x1 == x2):  # 가로 -> 세로
            x1, y1 = n - y1 - 1, x1
            x2, y2 = n - y2 - 1, x2

        rotate_corss.append((x1, y1))
        rotate_corss.append((x2, y2))

    # for i in range(len(cross)):
    #     before_x, before_y = cross[i][0], cross[i][1]
    #     after_x, after_y = rotate_corss[i][0], rotate_corss[i][1]
    #
    #     matrix[after_x][after_y] = matrix[before_x][before_y]

    before = []
    for i in range(len(cross)):
        before_x, before_y = cross[i][0], cross[i][1]
        before.append(matrix[before_x][before_y])

    for i in range(len(before)):
        after_x, after_y = rotate_corss[i][0], rotate_corss[i][1]
        matrix[after_x][after_y] = before[i]


# 정사각형 회전
def sq_rotate(x, y):
    rotate_sq = []

    before = []
    for i in range(x, x+sn):
        for j in range(y, y+sn):
            ox, oy = i - x, j - y       # (0, 0)으로 변환
            rx, ry = oy, sn - ox - 1    # 시계 방향 회전 공식

            before.append(matrix[i][j])
            rotate_sq.append((rx + x, ry + y))

    for i in range(len(rotate_sq)):
        after_x, after_y = rotate_sq[i][0], rotate_sq[i][1]
        matrix[after_x][after_y] = before[i]


## 사각형 회전 이전 버전
"""
def square_rotate(start, end):
    # 00 11 / 03 41 / 30 14 / 33 44
    square_list = []  # 돌리기 전 사각형 인덱스 담기
    rotate_sq = []  # 돌린 후의 사각형 인덱스 담기

    start_x, start_y = start[0], start[1]
    end_x, end_y = end[0], end[1]

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            square_list.append((i, j))

    for i in range(len(square_list)):
        x, y = square_list[i][0], square_list[i][1]
        rotate_sq.append((y, sn - 1 - x))

    # 1번 사각형 회전
    before = []
    for i in range(len(square_list)):
        before_x, before_y = square_list[i][0], square_list[i][1]
        before.append(matrix[before_x][before_y])

    for i in range(len(before)):
        after_x, after_y = rotate_sq[i][0], rotate_sq[i][1]
        matrix[after_x][after_y] = before[i]

    # global rotate_form
    #
    # if(len(rotate_form) > 0):
    #     for i in range(start_x, end_x + 1):
    #         for j in range(start_y, end_y + 1):
    #             square_list.append((i, j))
    #     for i in range(len(rotate_form)):
    #         rotate_sq.append((rotate_form[i][0] + square_list[i][0], rotate_form[i][1] + square_list[i][1]))
    #
    # if(len(rotate_form) == 0):
    #     for i in range(start_x, end_x + 1):
    #         for j in range(start_y, end_y + 1):
    #             square_list.append((i, j))
    #             rotate_sq.append((j, sn - 1 - i))
    #
    # if (start_x == 0 and start_y == 0):
    #     rotate_form = rotate_sq

    # for i in range(len(square_list)):
        # x, y = square_list[i][0], square_list[i][1]
        # rotate_sq.append((y, sn - 1 - x))

    # 돌리기
    before = []
    for i in range(len(square_list)):
        before_x, before_y = square_list[i][0], square_list[i][1]
        before.append(matrix[before_x][before_y])

    for i in range(len(before)):
        after_x, after_y = rotate_sq[i][0], rotate_sq[i][1]
        matrix[after_x][after_y] = before[i]
"""

### 실행
for _ in range(4):
    # 그룹 만들기
    check_visit = [[0 for i in range(n)] for j in range(n)]     # 방문하는 노드를 기록할 배열 따로 선언 (그룹 만들기 전 초기화)
    group.clear()       # 새로운 그룹 만들기 전 초기화

    # bfs로 그룹 만들기
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            make_group(i, j)

    # print(group)
    # print("==")

    # 조화로움 모두 더하기
    for i in range(len(group)):
        if (i + 1 > len(group)):
            break
        for j in range(i + 1, len(group)):
            group1, group2 = group[i], group[j]
            group1_num, group2_num = matrix[group[i][0][0]][group[i][0][1]], matrix[group[j][0][0]][group[j][0][1]]

            w = get_meeting_wall(group1, group2)  # 인접하는 변의 수 구하기

            answer += cal_point(group1, group2, group1_num, group2_num, w)  # 조화로움 계산


    # 십자가 선택 + 회전
    select_cross_rotate()

    ## 사각형 선택 (시작점, 끝점 파악)
    # sqaure_s_e = []
    # for i in range(0, n, sn + 1):
    #     for j in range(0, n, sn + 1):
    #         start = (i, j)
    #         end = (i + sn - 1, j + sn - 1)
    #         sqaure_s_e.append([start, end])  # 각 사각형의 시작, 끝 인덱스 담기
    #
    # print(sqaure_s_e)
    #
    # for i in range(len(sqaure_s_e)):
    #     s, e = sqaure_s_e[i][0], sqaure_s_e[i][1]
    #     # square_rotate(s, e)
    #     sq_rotate(s, e)

    # 사각형 회전
    sq_rotate(0, 0)
    sq_rotate(0, sn + 1)
    sq_rotate(sn + 1, 0)
    sq_rotate(sn + 1, sn + 1)

    # print(answer)
    # print(matrix)

print(answer)


""" 제출 버전 (6번 테케 실패) """
######################################

# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]

# # print(matrix)

# d = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 좌상우하
# group = []

# answer = 0

# sn = n // 2     # 선택되는 정사각형의 한 변


# ## 범위를 벗어나는지 판단하는 함수
# def check_range(x, y):
#     if (x < 0 or y < 0 or x >= n or y >= n):
#         return False
#     else:
#         return True


# ## 그룹 만들기
# def make_group(i, j):
#     start = matrix[i][j]  # 초기값
#     check_visit[i][j] = 1
#     sub_arr = [(i, j)]  # 만들어지는 그룹을 저장할 배열
#     arr = [(i, j)]  # 상하좌우를 탐색해야할 인덱스
#     while (arr):
#         i, j = arr.pop(0)
#         for l in range(len(d)):  # 상하좌우에 같은게 있는지 보기
#             dx, dy = d[l][0], d[l][1]
#             x, y = i + dx, j + dy

#             if (check_range(x, y)):
#                 if (check_visit[x][y] == 0):
#                     if (matrix[x][y] == start and (x, y) not in sub_arr):  # 같은거 있으면 그룹에 추가
#                         sub_arr.append((x, y))
#                         arr.append((x, y))
#                         start = matrix[x][y]
#                         check_visit[x][y] = 1

#     # 이미 그룹화 되어있는 애면 최종 그룹에 추가하지 않음
#     for i in range(len(sub_arr)):
#         for j in range(len(group)):
#             if (sub_arr[i] in group[j]):
#                 return

#     group.append(sub_arr)


# ## 맞닿은 변의 개수 구하는 함수
# def get_meeting_wall(group1, group2):
#     result = 0

#     for i in range(len(group1)):
#         row, col = group1[i][0], group1[i][1]
#         for l in range(len(d)):
#             dx, dy = d[l][0], d[l][1]
#             x, y = row + dx, col + dy
#             if (check_range(x, y)):
#                 if ((x, y) in group2):
#                     result += 1
#     return result


# ## 조화로움 점수 계산하는 함수
# def cal_point(group1, group2, group1_num, group2_num, meeting_wall):
#     return (len(group1) + len(group2)) * group1_num * group2_num * meeting_wall


# ## 십자가 선택하고 회전
# def select_cross_rotate():
#     # 십자가 인덱스 담기
#     arr = []
#     for i in range(n):
#         if (i != n // 2):
#             arr.append((i, n // 2))
#             arr.append((n // 2, i))
#     cross = sorted(list(set(arr)))

#     # 회전하기
#     rotate_corss = []
#     for i in range(0, len(cross), 2):
#         if (i + 1 > len(cross)):
#             break
#         x1, y1 = cross[i][0], cross[i][1]
#         x2, y2 = cross[i + 1][0], cross[i + 1][1]

#         if (y1 == y2):  # 세로 -> 가로
#             x1, y1 = y1, x1
#             x2, y2 = y2, x2
#         elif (x1 == x2):  # 가로 -> 세로
#             x1, y1 = n - y1 - 1, x1
#             x2, y2 = n - y2 - 1, x2

#         rotate_corss.append((x1, y1))
#         rotate_corss.append((x2, y2))

#     before = []
#     for i in range(len(cross)):
#         before_x, before_y = cross[i][0], cross[i][1]
#         before.append(matrix[before_x][before_y])

#     for i in range(len(before)):
#         after_x, after_y = rotate_corss[i][0], rotate_corss[i][1]
#         matrix[after_x][after_y] = before[i]


# def sq_rotate(x, y):
#     rotate_sq = []
#     ###########
#     before = []
#     for i in range(x, x+sn):
#         for j in range(y, y+sn):
#             ox, oy = i - x, j - y       # (0, 0)으로 변환
#             rx, ry = oy, sn - ox - 1    # 시계 방향 회전 공식

#             before.append(matrix[i][j])
#             rotate_sq.append((rx + x, ry + y))
#     ###########
#     for i in range(len(rotate_sq)):
#         after_x, after_y = rotate_sq[i][0], rotate_sq[i][1]
#         matrix[after_x][after_y] = before[i]

# ### 실행
# for _ in range(4):
#     # 그룹 만들기
#     check_visit = [[0 for i in range(n)] for j in range(n)]     # 방문하는 노드를 기록할 배열 따로 선언 (그룹 만들기 전 초기화)
#     group.clear()       # 새로운 그룹 만들기 전 초기화

#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             make_group(i, j)

#     # 조화로움 모두 더하기
#     for i in range(len(group)):
#         if (i + 1 > len(group)):
#             break
#         for j in range(i + 1, len(group)):
#             group1, group2 = group[i], group[j]
#             group1_num, group2_num = matrix[group[i][0][0]][group[i][0][1]], matrix[group[j][0][0]][group[j][0][1]]

#             w = get_meeting_wall(group1, group2)  # 인접하는 변의 수 구하기

#             answer += cal_point(group1, group2, group1_num, group2_num, w)  # 조화로움 계산

#     # 십자가 선택 + 회전
#     select_cross_rotate()

#     sq_rotate(0, 0)
#     sq_rotate(0, sn + 1)
#     sq_rotate(sn + 1, 0)
#     sq_rotate(sn + 1, sn + 1)

#     # print(answer)
#     # print(matrix)

# print(answer)