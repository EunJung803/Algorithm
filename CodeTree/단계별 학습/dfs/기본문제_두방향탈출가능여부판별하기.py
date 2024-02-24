n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [list(0 for _ in range(m)) for _ in range(n)]     # 각 격자의 방문 여부를 체크할 2차원 배열

ans = []    # 갈 수 있는 좌표값 (x, y) 를 담을 배열

# 갈 수 있는 격자인지 판별해주는 함수
def can_go(x, y):
    if(x >= n or y >= m or x < 0 or y < 0):         # 범위를 벗어나면 X
        return False
    if(visited[x][y] == -1 or matrix[x][y] == 0):   # 이미 방문한 곳이거나, 뱀이 있는 곳이라면 X
        return False
    return True

# DFS 실행
def dfs(x, y):
    # 아래로 이동, 오른쪽으로 이동
    dx = [1, 0]
    dy = [0, 1]

    for i, j in zip(dx, dy):
        new_x = x + i   # 이동할 X 좌표
        new_y = y + j   # 이동할 Y 좌표

        if(can_go(new_x, new_y)):       # (이동할 X, 이동할 Y)가 갈 수 있는 격자라면 -> 이동
            visited[new_x][new_y] = -1
            ans.append((new_x, new_y))
            # print(ans)
            dfs(new_x, new_y)

# 초기 시작 (좌측 상단인 (0,0) 에서부터 시작)
visited[0][0] = -1
ans.append((0,0))
dfs(0, 0)

# print(ans)
if((n-1, m-1) in ans):
    print(1)
else:
    print(0)