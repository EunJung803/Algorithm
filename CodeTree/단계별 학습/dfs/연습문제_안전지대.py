import sys
sys.setrecursionlimit(2500)     # maximum recursion depth exceed 에러 방지를 위해 최대 깊이 설정

## 입력 받기
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# n * m 사이즈의 k 수에 따라서 방문하게 될 영역이 지정될 2차원 배열 (0 == 방문, 1 == 방문 불가)
k_map = [list(0 for _ in range(m)) for _ in range(n)]

# DFS 탐색을 위해 방문했는지 안했는지 체크하기 위한 2차원 배열
visited = [list(0 for _ in range(m)) for _ in range(n)]

## 변수 선언
k = 1
max_k = k

max_area = 0        # 최대 안전 영역의 수

safe_area = []      # 안전 영역의 좌표들을 담을 배열 (인접해있는 동일한 안전 영역 하나)
ans = []            # 현재 위치하고 있는 좌표를 기준으로 탐색한 안전 영역의 좌표들을 담을 배열 (영역들이 담김)
count_safe = []     # 안전 영역의 개수를 담을 배열 (영역의 개수가 담김)

## DFS 탐색 시 해당 좌표로 이동 가능한지 판별할 함수
def can_go(x, y):
    if(x < 0 or y < 0 or x >= n or y >= m):
        return False
    if(visited[x][y] == 1 or k_map[x][y] == 1):
        return False
    else:
        return True

## DFS 탐색
def dfs(x, y):
    # 상하좌우 이동 -> 안전한 영역 담기
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if(can_go(new_x, new_y)):   # 방문 가능한 좌표라면
            safe_area.append((new_x, new_y))    # 안전 영역 배열에 담기
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

## k 수에 따라서 방문 가능한 곳인지 아닌지 표시하는 함수
def check_k(k):
    # k 수에 해당되는 영역 체크
    for i in range(n):
        for j in range(m):
            if (matrix[i][j] == k):
                k_map[i][j] = 1
    return k_map

## main 수행
while(k <= 100):    # 모든 집의 높이는 100 이하이므로 100을 최대 기준으로 잡고 완탐 수행
    k_map = check_k(k)      # 현재 k 수에 대한 영역 체크

    # 안전 영역 카운트
    for x in range(n):
        for y in range(m):

            if(k_map[x][y] == 0 and visited[x][y] == 0):    # 방문 가능한 지역이면
                # 해당 (x, y) 를 시작점으로 잡고 -> DFS 수행
                visited[x][y] = 1
                safe_area.append((x, y))
                dfs(x, y)

                ans.append(safe_area)       # ans 배열에 현재까지 이동했던 안전 영역 담기
                safe_area = []              # 다음 안전 영역을 다시 담기 위해서 초기화

    visited = [list(0 for _ in range(m)) for _ in range(n)]     # 다음 방문을 위해 초기화

    count_safe.append(len(ans))     # 현재까지 담긴 안전 영역의 개수 count_safe 배열에 담기
    ans = []                        # 다음 안전 영역의 개수를 담기 위해서 초기화

    if(count_safe):
        if(max_area < max(count_safe)):     # 더 큰 안전 영역의 수가 존재한다면 -> 갱신하기
            max_area = max(count_safe)
            max_k = k

    k += 1

# print(count_safe)

## 정답 출력
print(max_k, max_area)