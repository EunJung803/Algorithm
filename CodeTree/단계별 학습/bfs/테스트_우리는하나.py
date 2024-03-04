from collections import deque
from itertools import combinations

n, k, u, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited_bfs = [list(0 for _ in range(n)) for _ in range(n)]

q = deque()

city = set()
ans = []

# k개 뽑는 조합을 구하기 위하여 각 격자의 [x좌표, y좌표, 값] 을 하나의 리스트로 모두 담아줌
arr = []
for i in range(n):
    for j in range(n):
        arr.append([i, j, matrix[i][j]])

pick_k_list = list(combinations(arr, k))    # 그 리스트에서 k개를 뽑는 조합 생성

def can_go(x, y, current, visited_bfs):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    if(visited_bfs[x][y] == 1):
        return False
    if(abs(matrix[x][y] - current) < u or abs(matrix[x][y] - current) > d):     # 두 도시의 차가 u이상, d이하 여야만 이동 가능
        return False
    else:
        return True

def bfs(q):
    visited_bfs = [list(0 for _ in range(n)) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        current_value = matrix[x][y]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if(can_go(new_x, new_y, current_value, visited_bfs)):
                visited_bfs[new_x][new_y] = 1
                city.add((new_x, new_y))
                q.append((new_x, new_y))

## Main 실행
# k개가 선택되는 조합 리스트에서 일단 모두 큐에 하나씩 담아줌 (== 우선 시작점 큐에 다 담기)
for i in range(len(pick_k_list)):
    for j in range(len(pick_k_list[i])):
        city.add((pick_k_list[i][j][0], pick_k_list[i][j][1]))
        q.append((pick_k_list[i][j][0], pick_k_list[i][j][1]))

    # 다 담고 해당 큐로 BFS 탐색 실행
    bfs(q)

    # 이동 가능한 도시들 좌표 리스트를 ans에 담아주고 갱신
    ans.append(city)
    city = set()

# 갈 수 있는 서로 다른 도시의 최대값 구하기
max_city = 0
for i in range(len(ans)):
    if(len(ans[i]) > max_city):
        max_city = len(ans[i])

print(max_city)     # 정답 출력