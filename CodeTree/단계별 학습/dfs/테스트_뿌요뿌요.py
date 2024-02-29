n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [list(0 for _ in range(n)) for _ in range(n)]

block = []      # 하나의 블럭을 이루는 좌표값 (x, y) 들을 담을 리스트
ans = []        # 각 블럭들이 모여있는 리스트를 하나로 담아둘 리스트

# 현재 같은 target(숫자)을 가지고 있고, 이동 가능한 위치인지 파악하는 함수
def can_go(x, y, target):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    if(matrix[x][y] != target or visited[x][y] == 1):
        return False
    else:
        return True

# DFS 탐색 수행
def dfs(x, y, target):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if(can_go(new_x, new_y, target)):
            visited[new_x][new_y] = 1
            block.append((new_x, new_y))
            dfs(new_x, new_y, target)

# Main 실행
for a in range(n):
    for b in range(n):
        if(visited[a][b] == 0):     # 현재 위치가 방문 가능한 곳이라면 -> 인접한 같은 숫자가 있는지 DFS로 블럭 찾기
            visited[a][b] = 1
            block.append((a, b))

            dfs(a, b, matrix[a][b])

            ans.append(block)       # 모인 블럭들을 ans에 담기
        block = []      # 다음에 담을 블럭을 위해서 초기화


block_cnt = 0   # 터지게 되는 블럭 수를 담을 변수
max_sq = 0      # 최대 블럭의 크기를 담을 변수

# 정답 출력을 위한 계산
for i in range(len(ans)):
    if(len(ans[i]) >= 4):       # 블럭이 4칸 이상이라면 터짐
        block_cnt += 1
    if(len(ans[i]) > max_sq):   # 최대 블럭보다 큰 블럭이 존재하면 -> 갱신
        max_sq = len(ans[i])

# print(ans)
print(block_cnt, max_sq)