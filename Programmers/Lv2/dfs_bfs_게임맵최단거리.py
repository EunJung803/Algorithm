from collections import deque

# BFS로 풀이
# def solution(maps):
#     answer = 0
#
#     # 상 하 좌 우
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     q = deque()         # 큐 선언 (이동 가능한 위치의 좌표를 담을 큐)
#     q.append((0, 0))
#
#     while(q):   # 큐가 빌 때까지 반복
#         x, y = q.popleft()      # 왼쪽에서부터 꺼내서 해당 위치에서 상하좌우 이동 가능한지 판단하기
#
#         for i in range(4):
#             nx = x + dx[i]      # (상하좌우 순서대로) 이동 후의 x좌표
#             ny = y + dy[i]      # (상하좌우 순서대로) 이동 후의 y좌표
#
#             if(nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0])):      # 맵 범위를 벗어나면 X
#                 continue
#             if(maps[nx][ny] == 0 or (nx == 0 and ny == 0)):     # 벽이 있으면 X, 시작점으로 다시 이동 X
#                 continue
#             if(maps[nx][ny] == 1):      # 이동 가능한 위치 + 아직 방문하지 않은 지점이라면
#                 maps[nx][ny] = maps[x][y] + 1       # 현재까지의 거리로 업데이트
#                 q.append((nx, ny))                  # 해당 위치는 이동 가능하므로 큐에 삽입
#
#     # for i in range(len(maps)):
#     #     print(maps[i])
#
#     answer = maps[-1][-1]       # 최종 상대방 칸 위치에 있는 값이 정답인 최단거리값
#
#     # 1이라면 도착하지 못했다는 뜻이므로 -1 반환
#     if(answer == 1):
#         return -1
#
#     return answer

# 240319 풀이 추가
from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    def check_range(x, y):
        if (x < 0 or y < 0 or x >= n or y >= m):
            return False
        return True

    answer = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = [list(0 for _ in range(m)) for _ in range(n)]
    record = [list(0 for _ in range(m)) for _ in range(n)]

    q = deque()
    q.append([0, 0, answer])
    visited[0][0] = 1

    while (q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        cnt = curr[2]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (check_range(nx, ny) and visited[nx][ny] == 0 and maps[nx][ny] == 1):
                visited[nx][ny] = 1
                q.append([nx, ny, cnt + 1])
                record[nx][ny] = cnt + 1
                answer = cnt + 1

    if (record[n - 1][m - 1] == 0):
        return -1

    answer = record[n - 1][m - 1]

    return answer

if __name__ == '__main__':
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))