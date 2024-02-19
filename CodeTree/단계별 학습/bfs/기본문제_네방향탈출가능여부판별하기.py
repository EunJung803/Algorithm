from collections import deque

n, m = map(int, input().split())    # n, m 입력받기
matrix = [list(map(int, input().split())) for _ in range(n)]    # 2차원 배열 입력받기 (0 == 뱀이 있음, 1 == 뱀이 없음)

visited = [[0 for _ in range(m)] for _ in range(n)]     # 이동한 구역 체크용 2차원 배열
ans = [[0 for _ in range(m)] for _ in range(n)]         # bfs대로 이동 순서 체크용 2차원 배열

# 이동 가능한지 판단하는 함수
def can_go(x, y):
    if(x < 0 or x >= n or y < 0 or y >= m):
        return False
    if(visited[x][y] == 1 or matrix[x][y] == 0):
        return False
    return True

# 큐 선언
q = deque()

# 초기 실행
num = 1     # 방문 순서 기록용
q.append([0, 0])
visited[0][0] = 1
ans[0][0] = num

# 이동 방향 (상, 좌, 하, 우)
dx_list = [-1, 0, 1, 0]
dy_list = [0, -1, 0, 1]

# bfs 탐색 실행
while(q):
    x, y = q.popleft()
    for dx, dy in zip(dx_list, dy_list):
        new_x = x + dx
        new_y = y + dy

        if(can_go(new_x, new_y)):
            num += 1
            ans[new_x][new_y] = num
            q.append([new_x, new_y])
            visited[new_x][new_y] = 1

# print(visited)
# print(ans)

# 정답출력 ) 뱀에게 물리지 않고 탈출 가능한 경로가 있으면 1, 없으면 0을 출력
if(ans[n-1][m-1] == 0):
    print(0)
else:
    print(1)