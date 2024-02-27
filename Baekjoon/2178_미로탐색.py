from collections import deque

# 입력 받기
N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

visited = [list(0 for _ in range(M)) for _ in range(N)]     # 방문 체크용 배열
ans = [list(0 for _ in range(M)) for _ in range(N)]         # 방문 순서 확인용 배열

q = deque()     # 큐 선언

# 이동 가능한 좌표인지 확인하는 함수
def can_go(x, y):
    if(x < 0 or y < 0 or x >= N or y >= M):
        return False
    if(matrix[x][y] == 0 or visited[x][y] == 1):
        return False
    else:
        return True

# # (0,0) 시작
q.append((0, 0, 1))
visited[0][0] = 1
ans[0][0] = 1

# 방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS 탐색
while(q):
    curr_point = q.popleft()    # 현재 위치

    x = curr_point[0]
    y = curr_point[1]
    curr_move_cnt = curr_point[2]       # 현재 이동한 횟수

    ans[x][y] = curr_move_cnt       # 큐에서 꺼낸 (x, y) 이동 가능하므로 담겼기 때문에 방문 순서 확인을 위해 ans배열에 이동 횟수 넣어주기

    # 상하좌우 탐색
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        # 이동 가능하다면 -> 현재 이동한 횟수+1 을 해서 큐에 해당 좌표 담아주기, 재탐색하지 않도록 방문 처리
        if(can_go(new_x, new_y)):
            q.append((new_x, new_y, curr_move_cnt+1))
            visited[new_x][new_y] = 1

# 방문 순서 확인을 위한 출력
# for i in range(len(ans)):
#     print(ans[i])

# 정답 출력
print(ans[N-1][M-1])