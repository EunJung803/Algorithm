from collections import deque

n = int(input())
v = int(input())
network = [list(map(int, input().split())) for _ in range(v)]

graph = [[] for _ in range(n+1)]

for i in range(len(network)):
    graph[network[i][0]].append(network[i][1])
    graph[network[i][1]].append(network[i][0])

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력

visited = [0 for _ in range(n+1)]

q = deque()
q.append(graph[1])
visited[1] = 1

cnt = 0

while(q):
    curr = q.popleft()

    for next in curr:
        if(visited[next] == 0):
            visited[next] = 1
            q.append(graph[next])
            cnt += 1

print(cnt)