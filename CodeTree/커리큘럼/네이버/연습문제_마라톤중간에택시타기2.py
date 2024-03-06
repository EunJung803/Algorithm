N = int(input())
check_points = [list(map(int, input().split())) for _ in range(N)]

ans = []

# 들어온 arr의 모든 거리를 합하며 총 거리 계산하여 return
def get_total_dist(arr):
    total_dist = 0
    for i in range(len(arr)):
        if (i < len(arr)-1):
            p1 = arr[i]
            p2 = arr[i + 1]

            total_dist += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return total_dist

for i in range(1, N-1):
    to_jump = check_points[i]       # 건너뛸 체크포인트 선정
    tmp = []
    for j in range(N):
        if(check_points[j] != to_jump and i != j):
            tmp.append(check_points[j])         # 건너뛰는 체크포인트 제외하고 다 방문하므로 tmp리스트에 담아두기

    dist = get_total_dist(tmp)      # 총 거리 계산

    ans.append(dist)

print(min(ans))     # 정답으로 최소 거리 출력