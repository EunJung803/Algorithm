from collections import deque

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

q = deque()
visited = [list(0 for _ in range(N)) for _ in range(N)]

def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    return True

def bfs():
    town = []
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if(check_range(nx, ny) and visited[nx][ny] == 0 and matrix[nx][ny] == 1):
                visited[nx][ny] = 1
                q.append([nx, ny])
                town.append([nx, ny])
    return town

## 각 단지 탐색해서 하나로 담기
total = []
for i in range(N):
    for j in range(N):
        t = []
        if(matrix[i][j] == 1):
            q.append([i, j])
            t = bfs()
            if(t):
                total.append(len(t))

## 정답 출력
print(len(total))
total.sort()    # 오름차순으로 정렬
for tt in total:
    print(tt)

# print(' '.join(map(str, total)))