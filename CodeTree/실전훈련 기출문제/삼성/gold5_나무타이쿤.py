from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
move_rule = [list(map(int, input().split())) for _ in range(M)]

# → ↗ ↑ ↖ ← ↙ ↓ ↘
d = [(), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)]

# 범위 확인 함수
def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    return True

# 대각선에 인접한 높이 1 이상의 리브로수의 개수 확인 함수
def check_diagonal(x, y):
    dia = [(-1,1), (-1,-1), (1,-1), (1,1)]
    cnt = 0
    for i in range(4):
        nx = x + dia[i][0]
        ny = y + dia[i][1]
        if(check_range(nx, ny) and matrix[nx][ny] >= 1):
            cnt += 1
    return cnt

# 초기 영양제 배치
nutrients = [list(0 for _ in range(N)) for _ in range(N)]   # 영양제 위치 배열
nutrients[N-1][0] = 1
nutrients[N-2][0] = 1
nutrients[N-1][1] = 1
nutrients[N-2][1] = 1

q = deque([(N-1, 0), (N-2, 0), (N-1, 1), (N-2, 1)])
year = 0

# 이동 규칙대로 이동
for mr in move_rule:
    if(year == M):
        break

    # mr[0]   # 방향
    # mr[1]   # 칸수

    dx = d[mr[0]][0] * mr[1]    # 이동할 x칸
    dy = d[mr[0]][1] * mr[1]    # 이동할 y칸

    # 영양제 이동
    moved_idx = []
    while (q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        nx = (x + dx) % N
        ny = (y + dy) % N

        nutrients[x][y] = 0
        nutrients[nx][ny] = 1

        matrix[nx][ny] += 1     # 영양제 투입

        moved_idx.append((nx, ny))      # 이동 후의 영양제 위치 기억하기

    # 대각선 파악
    diagonal_list = []
    for i in range(len(moved_idx)):
        x = moved_idx[i][0]
        y = moved_idx[i][1]
        diagonal_list.append(check_diagonal(x, y))

    # 파악한 1 이상의 리브로수만큼 성장
    for i in range(len(moved_idx)):
        x = moved_idx[i][0]
        y = moved_idx[i][1]
        matrix[x][y] = matrix[x][y] + diagonal_list[i]

    # 영양제 투입한 리브로수 제외하고 2 이상인 높이는 잘라내기 + 영양제 올려두기
    for i in range(N):
        for j in range(N):
            if((i,j) in moved_idx):
                nutrients[i][j] = 0     # 투입한 영양제는 사라짐
                continue
            if((i,j) not in moved_idx and matrix[i][j] >= 2):
                matrix[i][j] -= 2
                q.append((i, j))
                nutrients[i][j] = 1

    year += 1

# 정답 계산
ans = 0
for i in range(N):
    for j in range(N):
        ans += matrix[i][j]

print(ans)