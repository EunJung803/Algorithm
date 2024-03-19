from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1, 0]
dy = [1, -1, 0, 0, 0]

q = deque()

## 범위를 체크하는 함수
def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= M):
        return False
    return True

## 분리된 빙산들을 탐색하는 함수
def bfs_findPart(q, visited):
    arr = []
    while (q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        for d in range(5):
            nx = x + dx[d]
            ny = y + dy[d]
            if (check_range(nx, ny) and visited[nx][ny] == 0 and matrix[nx][ny] != 0):
                visited[nx][ny] = 1
                q.append([nx, ny])
                arr.append([nx, ny])
    return arr

## 주변 물의 개수를 찾아서 해당 빙산의 녹는 높이를 구하는 함수
def bfs_melting():
    while (q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        melting = 0

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (check_range(nx, ny) and matrix[nx][ny] == 0):
                melting += 1

        melting_matrix[x][y] = melting

# 정답으로 출력될 년수
cnt = 0

while(True):
    for i in range(N):
        for j in range(M):
            if(matrix[i][j] > 0):       # 빙산이라면 -> 큐에 삽입
                q.append([i, j])

    melting_matrix = [list(0 for _ in range(M)) for _ in range(N)]
    bfs_melting()       # 현재 빙산들의 녹는 높이 구하기

    # 구한 녹는 높이만큼 녹여주기
    for i in range(N):
        for j in range(M):
            if(melting_matrix[i][j] > 0):
                if(melting_matrix[i][j] > matrix[i][j]):
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i][j] - melting_matrix[i][j]

    # 녹았으니까 1년 지남 !
    cnt += 1

    # 현재 빙산들의 덩어리 수 확인
    visited = [list(0 for _ in range(M)) for _ in range(N)]
    total_glacier = []
    for i in range(N):
        for j in range(M):
            glacier = []
            if(matrix[i][j] > 0):
                q.append([i, j])
                glacier = bfs_findPart(q, visited)
                if(glacier):
                    total_glacier.append(glacier)

    # 두 덩어리 이상으로 분리된다면
    if(len(total_glacier) >= 2):
        print(cnt)
        break

    # 아직 두 덩어리 이상으로 분리되지 않았다면
    else:
        cnt_not_water = 0
        cnt_water = 0
        for i in range(N):
            for j in range(M):
                if(matrix[i][j] != 0):
                    cnt_not_water += 1
                if(matrix[i][j] == 0):
                    cnt_water += 1

        # 빙산이 다 녹을 때까지 분리되지 않은 경우
        if(cnt_not_water == N*M or cnt_water == N*M):
            print(0)
            break
        else:
            continue