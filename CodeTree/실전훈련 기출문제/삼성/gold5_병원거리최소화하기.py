N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

ppl_list = []
hospital_list = []

for i in range(N):
    for j in range(N):
        if(matrix[i][j] == 1):
            ppl_list.append((i, j))
        if(matrix[i][j] == 2):
            hospital_list.append((i, j))

def get_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

selected = []
answer = int(1e9)
def dfs(idx):
    global answer
    if(len(selected) == M):
        total = 0
        for p in range(len(ppl_list)):
            dist = N * N
            for h in range(len(selected)):
                dist = min(dist, get_dist(ppl_list[p], selected[h]))
            total += dist
        answer = min(answer, total)
        return answer

    for i in range(idx, len(hospital_list)):
        selected.append(hospital_list[i])
        dfs(i+1)
        selected.pop()


dfs(0)
print(answer)