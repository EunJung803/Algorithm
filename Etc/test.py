# n = 5
# matrix = [
#     [1, 2, 2, 3, 3],
#     [2, 2, 2, 3, 3],
#     [2, 2, 1, 3, 1],
#     [2, 2, 1, 1, 1],
#     [2, 2, 1, 1, 1]
# ]
#
# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# check_visit = [[0] * n for _ in range(n)]
#
# group = [[0] * n for _ in range(n)]     # 그룹 정보저장용
# group_cnt = 0
#
# def out_range(x, y):
#     if (x < 0 or y < 0 or x >= n or y >= n):
#         return False
#     else:
#         return True
#
# def bfs_group(x, y, group_num):
#     global group_cnt
#     q = []
#     q.append((x, y))
#     check_visit[x][y] = 1
#     group_cnt += 1
#
#     k = 0
#     while(k < len(q)):
#         sx, sy = q[k]
#         for i in range(len(dir)):
#             nx, ny = sx + dir[i][0], sy + dir[i][1]
#             if(out_range(nx,ny) and check_visit[nx][ny] == 0):
#                 if(group_num == matrix[nx][ny]):
#                     q.append((nx, ny))
#                     check_visit[nx][ny] = 1
#         k += 1
#
#     # 해당 그룹이 matrix에서 존재하는 인덱스에 그룹 정보 넣어두기
#     for sx, sy in q:
#         group[sx][sy] = [group_cnt, group_num, len(q)]      # [그룹 번호(G~), 그룹으로 이루어진 숫자, 그룹 안에 존재하는 요소 갯수]
#
#
# for i in range(n):
#     for j in range(n):
#         if not check_visit[i][j]:
#             bfs_group(i, j, matrix[i][j])
#
# print(group)

# N = int(input())    # 만들어질 배열의 크기
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
d =  [(0, -1), (1, 0), (0, 1), (-1, 0)]
N = 5

snail = [[0] * N for _ in range(N)]     # 달팽이 배열의 크기 설정 (N * N)

r, c = 0, 0     # 달팽이 배열에 값을 채워넣기 위한 인덱스를 담을 변수 (현재 위치)
dist = 0        # dr, dc의 인덱스를 담을 변수 (0 : 오른쪽 / 1 : 아래 / 2 : 왼쪽 / 3 : 위)
num = 1         # 현재 숫자

while(num <= N*N):
    snail[r][c] = num
    num += 1

    r += d[dist][0]
    c += d[dist][1]

    if(r >= N or c >= N or r < 0 or c < 0 or snail[r][c] != 0):     # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있으면 방향 전환
        # 인덱스 재설정을 위해 실행 취소
        r -= d[dist][0]
        c -= d[dist][1]

        # 방향 전환
        dist = (dist + 1) % 4

        # 다시 수행
        r += d[dist][0]
        c += d[dist][1]

print(snail)