from itertools import combinations
from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# M개의 병원을 골라서 -> 바이러스를 전부 없애는데 걸리는 시간 중 -> 최소 시간을 구하기
# 0 : 바이러스 / 1 : 벽 / 2 : 병원

hospital = []
virus = []
for i in range(N):
    for j in range(N):
        if(matrix[i][j] == 2):          # 병원 인덱스 담기
            hospital.append((i, j))
        if (matrix[i][j] == 0):         # 바이러스 인덱스 담기
            virus.append((i,j))

combi_list = list(combinations(hospital, M))      # M개의 병원을 고르는 조합을 만들기

q = deque()

dx = [0,0,1,-1]
dy = [-1,1,0,0]

## 범위 확인 함수
def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    if(matrix[x][y] == 1):  # 벽이면 이동 불가
        return False
    return True

## 최단 경로 visited에 저장하며 탐색
def bfs():
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        cnt = curr[2]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if(check_range(nx, ny) and visited[nx][ny] > 0):        # 다른 병원에서 이미 방문했던 위치라면 -> 둘 중 최단 거리로 갱신
                visited[nx][ny] = min(visited[nx][ny], cnt + 1)
                continue
            if(check_range(nx, ny) and visited[nx][ny] == 0):
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = cnt + 1
                continue

## 정답 도출을 위한 함수
def find_answer():
    answer = 0
    cnt = 0
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if((i, j) in virus and visited[i][j] != 0):     # 바이러스 리스트에 존재하는 인덱스라면 -> 정답 찾기
                cnt += 1
                answer = max(answer, visited[i][j])
    if(cnt != len(virus)):      # 모든 바이러스를 없애지 못했다면 -1
        answer = -1
    return answer

## Main 실행
if(virus == 0):
    print(0)
else:
    result = []
    for i in range(len(combi_list)):
        visited = [list(0 for _ in range(N)) for _ in range(N)]
        for j in range(len(combi_list[i])):
            x = combi_list[i][j][0]
            y = combi_list[i][j][1]
            q.append((x, y, 0))
            visited[x][y] = 1
        bfs()

        tmp = find_answer()
        result.append(tmp)

    # result에 저장해둔 정답을 탐색하기
    cnt = 0
    answer = N * N
    for r in range(len(result)):
        if(result[r] == -1):
            cnt += 1
        else:
            answer = min(answer, result[r])     # 최단 거리였던 경우 찾아서 갱신

    if(cnt == len(combi_list)):     # 모든 바이러스를 없앨 수 있는 방법이 없는 경우
        print(-1)
    else:
        print(answer)