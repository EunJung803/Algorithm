n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
start_point = [list(map(int, input().split())) for _ in range(k)]

visited = [list(0 for _ in range(n)) for _ in range(n)]

count = 0

def can_go(x, y):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    if(matrix[x][y] == 1 or visited[x][y] == 1):
        return False
    else:
        return True

while(start_point):
    start = start_point.pop(0)      # 좌표들을 하나씩 뽑으며 수행

    dx = [0, 0, 1, 0, -1]       # 현재 시작값 위치 + 상하좌우
    dy = [0, 1, 0, -1, 0]

    x = start[0]-1
    y = start[1]-1

    for i in range(5):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if(can_go(new_x, new_y)):           # 갈 수 있는 곳이라면 -> 방문 처리
            visited[new_x][new_y] = 1
            start_point.append([new_x + 1, new_y + 1])      # BFS 탐색을 위해 큐에 넣기
            count += 1
    # print(count)

print(count)