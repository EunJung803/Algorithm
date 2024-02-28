from collections import defaultdict
from collections import deque

N, M, V = map(int, input().split())

node_list = [list(map(int, input().split())) for _ in range(M)]

# node_list 리스트를 돌면서, 각 정점에 연결되어있는 정점들을 리스트로 담음
node_dict = defaultdict(list)
for i in range(len(node_list)):
    # 양방향이기 때문에 모든 정점이 key로 담겨있어야함
    node_dict[node_list[i][0]].append(node_list[i][1])
    node_dict[node_list[i][0]].sort()       # 작은 정점 번호부터 방문해야 하므로 정렬시키기

    node_dict[node_list[i][1]].append(node_list[i][0])
    node_dict[node_list[i][1]].sort()       # 작은 정점 번호부터 방문해야 하므로 정렬시키기

# print(node_dict)

# 각 알고리즘에서 정점을 방문했는지 확인하기 위한 배열 선언
visited_dfs = list(0 for _ in range(N))
visited_bfs = list(0 for _ in range(N))

# 각 알고리즘의 정답을 담을 배열 선언
dfs_result = []
bfs_result = []

##########

# DFS 탐색
def dfs(node):
    curr_n = node_dict.get(node)
    if(curr_n):
        for i in range(len(curr_n)):
            to_go = curr_n[i]
            if(visited_dfs[to_go-1] == 0):
                visited_dfs[to_go-1] = 1
                dfs_result.append(to_go)
                dfs(to_go)

# 시작 정점인 V부터 탐색 시작
visited_dfs[V-1] = 1
dfs_result.append(V)
dfs(V)

print(' '.join(map(str, dfs_result)))       # DFS 정답 출력

##########

# BFS 탐색
q = deque()
def bfs(q):
    while(q):
        curr_n = node_dict.get(q.popleft())
        if(curr_n):
            for i in range(len(curr_n)):
                to_go = curr_n[i]
                if(visited_bfs[to_go-1] == 0):
                    visited_bfs[to_go-1] = 1
                    bfs_result.append(to_go)
                    q.append(to_go)

# 시작 정점인 V부터 탐색 시작
q.append(V)
visited_bfs[V-1] = 1
bfs_result.append(V)
bfs(q)

print(' '.join(map(str, bfs_result)))       # BFS 정답 출력