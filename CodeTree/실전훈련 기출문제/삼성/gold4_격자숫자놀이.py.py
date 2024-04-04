import copy
from collections import defaultdict

r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]

tmp_matrix = copy.deepcopy(matrix)

def make_new_row(arr):
    global max_len
    global new_matrix_row

    draft = []
    for i in range(len(arr)):
        count_num = defaultdict(int)    # 각 숫자의 출현횟수를 세기 용이하도록 defaultdict 사용

        # 각 행의 출현횟수 카운트
        for j in range(len(arr[i])):
            if(arr[i][j] != 0):
                count_num[arr[i][j]] += 1

        pair = []
        for key in count_num.keys():
            pair.append((key, count_num.get(key)))

        pair.sort()  # 숫자별로 정렬
        pair.sort(key=lambda x: x[1])  # 출현횟수 별로 정렬

        tmp = []
        for p in range(len(pair)):
            for pp in range(len(pair[p])):
                tmp.append(pair[p][pp])

        draft.append(tmp)
        max_len = max(max_len, len(tmp))  # 가장 큰 길이 기준

    for i in range(len(draft)):
        if (len(draft[i]) < max_len):  # 나머지 0으로 채우기
            for p in range(max_len - len(draft[i])):
                draft[i].append(0)
        new_matrix_row.append(draft[i])

def make_new_col(arr):
    global max_len
    global new_matrix_col

    # 열을 기준으로 카운트하기 위해서 회전시키기
    n = len(arr)
    m = len(arr[0])
    ret = [list(0 for _ in range(n)) for _ in range(m)]
    for i in range(n):
        for j in range(m):
            ret[j][n-i-1] = arr[i][j]

    draft = []
    for i in range(len(ret)):
        count_num = defaultdict(int)

        # 각 행의 출현횟수 카운트 (아까 뒤집어서 열을 행으로 바꿔놨으니)
        for j in range(len(ret[i])):
            if (ret[i][j] != 0):
                count_num[ret[i][j]] += 1

        pair = []
        for key in count_num.keys():
            pair.append((key, count_num.get(key)))

        pair.sort()  # 숫자별로 정렬
        pair.sort(key=lambda x: x[1])  # 출현횟수 별로 정렬

        tmp = []
        for p in range(len(pair)):
            for pp in range(len(pair[p])):
                tmp.append(pair[p][pp])

        draft.append(tmp)
        max_len = max(max_len, len(tmp))  # 가장 큰 길이 기준

    # 만들어진 draft를 열에서부터 차곡하게 쌓기
    col_tmp = [list(0 for _ in range(len(draft))) for _ in range(max_len)]
    for i in range(len(draft)):
        for j in range(len(draft[i])):
            col_tmp[j][i] = draft[i][j]

    new_matrix_col = copy.deepcopy(col_tmp)


## Main 실행
t = 0
get_ans = False

# 정답이 0인 경우 (바로 k를 찾은 경우)
if(r-1 < len(tmp_matrix) and c-1 < len(tmp_matrix[0])):
    if(tmp_matrix[r-1][c-1] == k):
        print(t)
        get_ans = True

# 그렇지 않은 경우
if(get_ans == False):
    while(t <= 100):
        t += 1

        new_matrix_row = []
        new_matrix_col = []
        max_len = 0

        row_len = len(tmp_matrix)       # 행 길이
        col_len = len(tmp_matrix[0])    # 열 길이

        # 행 >= 열
        if(row_len >= col_len):
            make_new_row(tmp_matrix)
            # print(new_matrix_row)

        # 행 < 열
        if(row_len < col_len):
            make_new_col(tmp_matrix)
            # print(new_matrix_col)

        if(new_matrix_row):
            tmp_matrix = copy.deepcopy(new_matrix_row)
        if(new_matrix_col):
            tmp_matrix = copy.deepcopy(new_matrix_col)

        # k를 찾았다면 정답 출력
        if(r-1 < len(tmp_matrix) and c-1 < len(tmp_matrix[0])):
            if(tmp_matrix[r-1][c-1] == k):
                print(t)
                get_ans = True
                break

    # 100초 초과
    if(get_ans == False):
        print(-1)
