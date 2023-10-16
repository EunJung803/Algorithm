# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]

n, m = 4, 1
matrix = [[15, 13, 1, 11],
[4, 8, 3, 5],
[2, 12, 16, 7],
[14, 6, 9, 10]]

# 상하좌우대각선 8방향 왼쪽 위부터 순서대로
d = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]

# 범위를 벗어나는지 확인
def check_range_out(x, y):
    if (x < 0 or y < 0 or x >= n or y >= n):
        return False
    else:
        return True


# 순차적으로 각 숫자의 인덱스 파악 (1부터 n까지)
def find_index(matrix):
    i_arr = []
    for i in range(n * n):  # 0 1 2 3 ... 15
        for j in range(len(matrix)):
            if (i + 1 in matrix[j]):
                i_arr.append([j, matrix[j].index(i + 1)])
                break
    return i_arr

# m번의 턴 실행
for _ in range(m):
    index_list = find_index(matrix)
    for r in range(len(index_list)):
        # print(r)
        # for row in matrix:
        #     for num in row:
        #         print(num, end=' ')
        #     print()
        # print("==")
        x, y = index_list[r][0], index_list[r][1]
        max_value = matrix[x][y]
        max_x, max_y = x, y

        # 초기 값 설정
        for a in range(len(d)):
            dx, dy = d[a][0], d[a][1]
            nx, ny = x + dx, y + dy
            if (check_range_out(nx, ny)):
                max_value = matrix[nx][ny]
                max_x, max_y = nx, ny
                break

        # 8방향 확인
        for j in range(len(d)):
            dx, dy = d[j][0], d[j][1]
            nx, ny = x + dx, y + dy
            if (check_range_out(nx, ny)):
                selected = matrix[nx][ny]
                if (selected > max_value):
                    max_value = selected
                    max_x, max_y = nx, ny

        # 교환
        tmp = matrix[x][y]
        matrix[x][y] = matrix[max_x][max_y]
        matrix[max_x][max_y] = tmp

        # 인덱스 업데이트
        index_list = find_index(matrix)

for row in matrix:
    for num in row:
        print(num, end=' ')
    print()
    print()