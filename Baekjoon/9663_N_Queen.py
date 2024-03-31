## 2차원 배열 사용 -> 시간 초과
# N = int(input())
#
# board = [list(0 for _ in range(N)) for _ in range(N)]
# count = 0
#
# def is_safe(board, row, col, N):
#     # 같은 열에 퀸이 있는지 확인
#     for i in range(row):
#         if board[i][col] == 1:
#             return False
#
#     # 왼쪽 위 대각선에 퀸이 있는지 확인
#     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False
#
#     # 오른쪽 위 대각선에 퀸이 있는지 확인
#     for i, j in zip(range(row, -1, -1), range(col, N)):
#         if board[i][j] == 1:
#             return False
#
#     return True
#
#
# def dfs(board, x, N, count):
#     if(x == N):
#         count += 1
#         return
#
#     for y in range(N):
#         if(is_safe(board, x, y, N)):
#             board[x][y] = 1
#             dfs(board, x+1, N, count)
#             board[x][y] = 0
#
#
# dfs(board, 0, N, count)
# print(count)

## 1차원 배열 사용
N = int(input())
cnt = 0

row = list(0 for _ in range(N))

def is_safe(num):
    for i in range(num):
        if(row[i] == row[num] or abs(row[i]-row[num]) == abs(i-num)):
            return False
    return True


def dfs(num):
    global cnt
    # print(num , row)
    if(num == N):
        cnt += 1
        return

    for i in range(N):
        row[num] = i        # 퀸을 [num, i] 자리에 놓음
        if(is_safe(num)):
            dfs(num + 1)

dfs(0)
print(cnt)