### 1. combinations로 조합 구해서 합의 최단거리 찾기
from itertools import combinations

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

home_list = []
chicken_list = []

for i in range(N):
    for j in range(N):
        if(matrix[i][j] == 1):
            home_list.append((i, j))
        if(matrix[i][j] == 2):
            chicken_list.append((i, j))

chicken_comb = list(combinations(chicken_list, M))
# print(chicken_comb)

def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

ans = int(1e9)
for i in range(len(chicken_comb)):
    total = 0
    for j in range(len(home_list)):
        chkn_dist = N*N
        for jj in range(len(chicken_comb[i])):
            chkn_dist = min(chkn_dist, get_dist(home_list[j], chicken_comb[i][jj]))
        total += chkn_dist
    ans = min(ans, total)

print(ans)

"""////////////"""

### 2. BFS로 각 집에서 최단거리를 가진 치킨집 찾기 + M개의 조합 구해서 합의 최단거리 찾기
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

q = deque()

def check_range(x,y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    return True

def get_dist(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return abs(x1-x2)+abs(y1-y2)

def find_all_chicken():
    chicken_dist = [0,0,N*N]
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        cnt = curr[2]

        if(city_map[x][y] == 2):
            if(cnt < chicken_dist[2]):
                chicken_dist = curr
            # chicken_dist.append(curr)
            # return curr

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(check_range(nx,ny) and visited[nx][ny] == 0):
                q.append([nx, ny, cnt+1])
                visited[nx][ny] = 1

    return chicken_dist

picked_chkn = set()
home_list = []
tmp_sum = 0

chkn_list = []

for i in range(N):
    for j in range(N):
        visited = [list(0 for _ in range(N)) for _ in range(N)]
        if(city_map[i][j] == 2):
            chkn_list.append((i, j))
        if(city_map[i][j] == 1):
            home_list.append((i, j))

            q.append([i, j, 0])
            visited[i][j] = 1

            chkn_dist = find_all_chicken()
            print(i, j, chkn_dist)
            tmp_sum += chkn_dist[2]

            picked_chkn.add((chkn_dist[0], chkn_dist[1]))

print(picked_chkn)
picked_chknLisk = list(picked_chkn)

if(len(picked_chknLisk) <= M):
    print(tmp_sum)

else:
    print(home_list)
    # 최대 M개를 골랐을 때, 가장 작은 도시 치킨 거리를 찾기
    pick_M = list(combinations(chkn_list, M))
    print(pick_M)

    ans = int(1e9)

    for i in range(len(pick_M)):
        total_dst = 0
        chkn = pick_M[i]
        for j in range(len(home_list)):
            dst = N*N
            for jj in range(len(chkn)):
                dst = min(dst, get_dist(home_list[j], chkn[jj]))
            total_dst += dst
        ans = min(ans, total_dst)
    print(ans)

"""////////////"""

### 3. DFS로 조합 구하기 + 완전 탐색
from collections import deque

N, M = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]

def get_dist(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return abs(x1-x2)+abs(y1-y2)

def dfs(n, num):
    global result
    city_chkn_dst = 0
    if(n == M):
        for ii in range(len(home_list)):
            final_dst = 2*N
            for jj in range(len(select_chkn)):
                dst = get_dist(home_list[ii], select_chkn[jj])
                if(dst < final_dst):
                    final_dst = dst
            city_chkn_dst += final_dst

        if(city_chkn_dst < result):
            result = city_chkn_dst
            return

    for d in range(num, len(chkn_list)):
        select_chkn.append(chkn_list[d])
        dfs(n+1, d+1)
        select_chkn.pop()


home_list = deque()
chkn_list = deque()

select_chkn = deque()

for i in range(N):
    for j in range(N):
        if(city_map[i][j] == 1):
            home_list.append((i,j))
        if(city_map[i][j] == 2):
            chkn_list.append((i,j))

# print(home_list)
# print(chkn_list)

result = 2 * N * len(home_list)

for i in range(len(chkn_list)):
    dfs(0, i)

print(result)