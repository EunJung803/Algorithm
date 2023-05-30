from collections import deque

N = int(input())  # N*N 배열 생성을 위한 값
matrix = [list(map(int, input().split())) for _ in range(N)]  # int 여러줄 입력받기 (2차원 배열로 저장)

# 모눈종이 전체를 탐색하며 BFS 진행
q = deque()
area = []
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            # matrix[i][j] = 1
            q.append((i, j))
            area.append(1)
            while (q):
                x, y = q.popleft()
                for a, b in move:
                    dx = x + a
                    dy = y + b
                    if N > dx >= 0 and N > dy >= 0 and not matrix[dx][dy]:
                        q.append((dx, dy))
                        matrix[dx][dy] = 1
                        area[-1] += 1

print(len(area))
print(*sorted(area))