from collections import defaultdict

## input 받기
n = int(input())
student_info = [list(map(int, input().split())) for _ in range(n * n)]

## n*n 배열 생성
matrix = [list(0 for _ in range(n)) for _ in range(n)]

## 점수 계산용 배열
score = [0, 1, 10, 100, 1000]

## 점수 계산을 용이하게 하기 위한 딕셔너리
student_dict = defaultdict(list)
for i in range(len(student_info)):
    student_dict[student_info[i][0]] = student_info[i][1:]

## 방향 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

## 범위 체크
def check_range(x, y):
    if (x < 0 or y < 0 or x >= n or y >= n):
        return False
    return True


## 모든 matrix 빈자리 중, 내가 좋아하는 친구가 얼마나 있는지 카운트, 인덱스랑 같이 담아서 리턴
def check_like(arr):
    like_list = []
    max_like = 0
    for i in range(n):
        for j in range(n):
            like_cnt = 0
            if (matrix[i][j] == 0):  # 현재 위치가 빈칸일때
                for d in range(4):  # 인접 탐색
                    x = i + dx[d]
                    y = j + dy[d]
                    if (check_range(x, y) and matrix[x][y] in arr):
                        like_cnt += 1
                if (max_like <= like_cnt):
                    like_list.append([i, j, like_cnt])
                    max_like = like_cnt
    return like_list


## 모든 matrix 빈자리 중, 현재 1번 조건을 만족하는 칸 중 주변에 빈칸이 몇개씩 있는지 탐색
def check_blank(arr):
    blank_list = []
    max_blank = 0

    for i in range(len(arr)):
        blank_cnt = 0
        x = arr[i][0]
        y = arr[i][1]
        if (matrix[x][y] == 0):
            for d in range(4):  # 인접 탐색
                nx = x + dx[d]
                ny = y + dy[d]
                if (check_range(nx, ny) and matrix[nx][ny] == 0):
                    blank_cnt += 1

        if (max_blank <= blank_cnt):
            blank_list.append([arr[i][0:2], blank_cnt])
            max_blank = blank_cnt
    return blank_list

## 놀이기구 탑승하기
for i in range(len(student_info)):
    curr_stu = student_info[i][0]   # 현재 학생번호
    like_stu = student_info[i][1:]  # 그 학생이 좋아하는 학생들 번호

    ## >>> 1번 조건
    # 현재 학생번호가 좋아하는 학생들이 인근에 얼마나 있는지 카운트
    get_like = check_like(like_stu)
    get_like.sort(key=lambda x: x[2], reverse=True)     # 내림차순 정렬

    max_like = get_like[0][2]           # 가장 많은 좋아하는 학생 수
    like_list = []
    for j in range(len(get_like)):      # max_like 값을 가진 인덱스 구하기
        if(get_like[j][2] == max_like):
            like_list.append([get_like[j][0], get_like[j][1]])

    # 그런 자리가 1자리라면 -> 해당 자리에 학생 들어가기
    if (len(like_list) == 1):
        matrix[like_list[0][0]][like_list[0][1]] = curr_stu

    ## >>> 2번 조건
    # 그런 자리가 2자리 이상이면 -> 빈칸으로 따지기
    if (len(like_list) >= 2):
        get_blank = check_blank(like_list)      # 인접한 칸 중 많은 빈칸의 수를 가진 인덱스 찾기
        get_blank.sort(key=lambda x: x[1], reverse=True)    # 내림차순 정렬

        max_blank = get_blank[0][1]         # 가장 많은 인접한 칸
        blank_list = []
        for j in range(len(get_blank)):     # max_blank 값을 가진 인덱스 구하기
            if(get_blank[j][1] == max_blank):
                blank_list.append(get_blank[j][0])

        # 그런 자리가 1자리라면 -> 해당 자리에 학생 들어가기
        if(len(blank_list) == 1):
            matrix[blank_list[0][0]][blank_list[0][1]] = curr_stu

        ## >>> 3번, 4번 조건
        # 그런 자리가 2자리 이상이면 -> 행 최소, 열 최소 인 곳으로 들어가기
        if(len(blank_list) >= 2):
            s = sorted(blank_list)
            matrix[s[0][0]][s[0][1]] = curr_stu

## 점수 계산하기
answer = 0
for i in range(n):
    for j in range(n):
        curr = matrix[i][j]
        like_list = student_dict[curr]
        like_cnt = 0
        for d in range(4):
            x = i + dx[d]
            y = j + dy[d]
            if (check_range(x, y) and matrix[x][y] in like_list):
                like_cnt += 1
        answer += score[like_cnt]

print(answer)
