from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def check_range(x, y):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    return True

def get_gold(arr):
    cnt_gold = 0
    for i in range(len(arr)):
        loc = arr[i]
        if (matrix[loc[0]][loc[1]] == 1):
            cnt_gold += 1
    return cnt_gold

# k번 이내로 인접한 곳으로 이동 가능한 BFS
def bfs(q, visited, curr_k):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while (q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        k = curr[2]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (check_range(nx, ny) and visited[nx][ny] == 0 and k+1 <= curr_k):
                q.append((nx, ny, k+1))
                visited[nx][ny] = 1
                bfs_list.append((nx, ny, k+1))
    return bfs_list

## main
k = 0
bfs_list = []

q = deque()

curr_k = 0
max_gold = 0
answer = 0

for i in range(n):
    for j in range(n):
        for kk in range(n+1):
            curr_k = kk

            visited = [list(0 for _ in range(n)) for _ in range(n)]
            center = (i, j, k)
            visited[i][j] = 1

            bfs_list = []
            bfs_list.append(center)

            q.append(center)

            bfs_list = bfs(q, visited, curr_k)

            cost = (curr_k * curr_k + (curr_k + 1) * (curr_k + 1))      # 비용
            earn = get_gold(bfs_list)       # 수익

            # 손해가 없다면 -> 최댓값을 정답으로
            if (cost <= earn * m):
                answer = max(answer, earn)

print(answer)