## input 받기
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

## 코드 수행을 위한 변수 선언
visited = [list(0 for _ in range(n)) for _ in range(n)]

village = []
ans = []

result = []

## 이동 가능한지 판별하는 함수
def can_go(x, y):
    if(x < 0 or x >= n or y < 0 or y >= n):
        return False
    if(visited[x][y] == 1 or matrix[x][y] == 0):
        return False
    else:
        return True

## dfs 수행
def dfs(x, y):
    # 하 우 상 좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):  # 상 하 좌 우 이동 가능한 좌표 찾기
        new_x = x + dx[i]
        new_y = y + dy[i]

        if(can_go(new_x, new_y)):   # 이동 가능하다면 -> 이동 후 dfs 재귀 수행
            visited[new_x][new_y] = 1
            village.append((new_x, new_y))  # 해당 좌표도 이동가능하므로 하나의 마을로 담기
            dfs(new_x, new_y)

## main 수행
for a in range(n):
    for b in range(n):
        if(matrix[a][b] == 1 and visited[a][b] == 0):   # 사람이 있고, 방문하지 않았다면 -> 마을 카운트의 시작점
            visited[a][b] = 1
            village.append((a, b))
            dfs(a, b)               # dfs 수행
            ans.append(village)     # 하나의 마을로 취급하여 묶어서 ans 배열에 추가
            village = []            # 다음 마을을 위해 배열 비우기

# print(ans)
# ans 배열에 담기는 형식은 아래와 같다
"""
[[(0, 0), (1, 0)], [(0, 2), (0, 3), (0, 4)], [(2, 3), (3, 3), (4, 3), (4, 4), (3, 4), (2, 4)], [(3, 0), (4, 0), (4, 1), (3, 1)]]
"""

## 정답 출력
# 정답 형식을 위해 result 배열에 값 넣기
for i in range(len(ans)):
    result.append(len(ans[i]))

print(len(result))      # 총 마을 개수

result.sort()   # 정답 출력을 위한 정렬 (오름차순)
for i in range(len(result)):    # 마을에 있는 사람 수 오름차순 출력
    print(result[i])