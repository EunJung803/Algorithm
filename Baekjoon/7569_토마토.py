from collections import deque

M, N, H = map(int, input().split())     # 가로 세로 높이
tomato = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]    # 가장 밑의 상자부터 가장 위의 상자까지

visited = [list(list(0 for _ in range(M)) for _ in range(N)) for _ in range(H)]

q = deque()

# 시작점을 위해서 큐에 초기 익은 토마토의 위치 담기
for h in range(H):
    for n in range(N):
        for m in range(M):
            if(tomato[h][n][m] == 1):
                q.append([h, n, m, 0])      # 높이, y, x, day
                visited[h][n][m] = 1
def check_range(z,x,y):
    if(z < 0 or z >= H or x < 0 or x >= M or y < 0 or y >= N):
        return False
    return True

d = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]       # (z, y, x) 인접

ans = 0     # 정답 일수를 담을 변수

## BFS 탐색
while(q):
    curr = q.popleft()
    z = curr[0]
    y = curr[1]
    x = curr[2]
    day = curr[3]

    for dd in d:
        nz = z + dd[0]
        ny = y + dd[1]
        nx = x + dd[2]
        if(check_range(nz,nx,ny) and tomato[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0):
            visited[nz][ny][nx] = 1
            tomato[nz][ny][nx] = 1
            q.append([nz, ny, nx, day+1])
            ans = day+1

# print(tomato)
# print(ans)

## 정답 출력
flag = True
for h in range(H):
    if(flag):
        for n in range(N):
            if (flag):
                for m in range(M):
                    if(tomato[h][n][m] == 0):       # 안익은 토마토가 있다면 -> -1
                        print(-1)
                        flag = False
                        break
if(flag):
    if(ans > 0):
        print(ans)
    else:
        print(0)