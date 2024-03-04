from collections import deque

N, M = map(int, input().split())
robot_x, robot_y, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 로봇청소기가 방문한 곳을 표시할 배열
visited = [list(0 for _ in range(M)) for _ in range(N)]

q = deque()
# move = []

# 북 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 범위 벗어나지 않는지 확인
def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= M):
        return False
    return True

# 주변 4칸 중에 청소해야하는 칸이 존재하는지 확인
def check_clean(x, y):
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (check_range(new_x, new_y) and matrix[new_x][new_y] == 0 and visited[new_x][new_y] == 0):
            return True
    return False

def bfs(q):
    global clean_cnt        # 청소한 영역의 개수를 담을 전역변수
    clean_cnt = 0

    while(q):
        curr = q.popleft()
        x = curr[0]         # 현재 로봇청소기의 x 좌표
        y = curr[1]         # 현재 로봇청소기의 y 좌표
        curr_d = curr[2]    # 현재 방향

        ## 현재 칸이 청소되지 않은 경우 (1번)
        if(visited[x][y] == 0):
            visited[x][y] = 1       # 현재 칸을 청소
            clean_cnt += 1
            # move.append((x, y))

        ## 현재 칸의 주변 4칸 비교
        # 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우 (3번)
        if(check_clean(x, y)):
            for _ in range(4):  # 청소되지 않은 빈칸으로 이동하기 전까지 반시계방향씩 회전하면서 방향 결정
                curr_d = (curr_d - 1) % 4  # 현재 방향에서 반시계방향 회전
                new_x = x + dx[curr_d]
                new_y = y + dy[curr_d]
                # 바라보는 방향에서 청소되지 않은 빈칸을 발견하면 -> 전진
                if (matrix[new_x][new_y] == 0 and visited[new_x][new_y] == 0):
                    q.append((new_x, new_y, curr_d))
                    break

        # 주변 4칸 중 청소되지 않은 빈 칸이 하나도 없는 경우 (2번)
        else:
            back_d = (curr_d + 2) % 4  # 후진하려는 방향
            new_x = x + dx[back_d]
            new_y = y + dy[back_d]
            if (matrix[new_x][new_y] == 0):         # 후진할 수 있다면 후진하고 1번으로 돌아가기
                q.append((new_x, new_y, curr_d))
            elif (matrix[new_x][new_y] == 1):       # 후진하려는 곳이 벽이라면 종료
                break

q.append((robot_x, robot_y, d))
bfs(q)

# print(move)
print(clean_cnt)