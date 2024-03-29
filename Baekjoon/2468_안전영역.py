from collections import deque

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 가장 높은 지역의 숫자 구하기
max_h = 0
for i in range(N):
    for j in range(N):
        if(max_h <= matrix[i][j]):
            max_h = matrix[i][j]

def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    return True

q = deque()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(q, target):
    area = []
    while(q):
        curr = q.popleft()
        area.append(curr)
        for d in range(4):
            nx = curr[0] + dx[d]
            ny = curr[1] + dy[d]
            if(check_range(nx,ny) and visited[nx][ny] == 0 and matrix[nx][ny] > target):
                q.append([nx,ny])
                visited[nx][ny] = 1
    return area

# 높이 1부터 잠긴다면 -> 안전영역 구하기
answer = 1
for i in range(1, max_h+1):
    visited = [list(0 for _ in range(N)) for _ in range(N)]
    ans = []
    for x in range(N):
        for y in range(N):
            area = []
            if(matrix[x][y] > i and visited[x][y] == 0):    # 잠기지 않을 지역이라면 -> 안전영역 탐색
                q.append([x, y])
                visited[x][y] = 1

                area = bfs(q, i)

                if(area):
                    ans.append(area)
                # print(i, area)

    answer = max(answer, len(ans))

print(answer)