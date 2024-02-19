N, M = map(int, input().split())        # N, M 입력받기
nodes = [list(map(int, input().split())) for _ in range(M)]     # 연결된 두 정점 입력받기

# 각 노드의 시작점, 끝점 구분해서 따로 담아두기
start_points = []
end_points = []
for i in range(len(nodes)):
    start_points.append(nodes[i][0])
    end_points.append(nodes[i][1])

# 2차원 배열 만들기
matrix = [[0 for _ in range(N)] for _ in range(N)]

for start, end in zip(start_points, end_points):
    matrix[start-1][end-1] = 1
    matrix[end-1][start-1] = 1

print(matrix)

# 방문한 노드 체크
visited = [False for _ in range(N)]

# dfs 재귀
def dfs(node):
    for curr_node in range(N):
        if(matrix[node][curr_node] and not visited[curr_node]):
            visited[curr_node] = True
            # print(visited)
            # print((node+1, curr_node+1))
            dfs(curr_node)

# 1이 루트노드로 시작
root_node = 0
visited[root_node] = True
dfs(root_node)

count = 0
for i in range(1, len(visited)):
    if(visited[i]):
        count += 1
print(count)