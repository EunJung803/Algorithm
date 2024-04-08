N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 0

start_point = (N//2, N//2)

def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    return True

# 좌 하 우 상
d = [(0,-1), (1,0), (0,1), (-1,0)]

# 이동하는 먼지 (좌 하 우 상)
m1 = [(1,1,1), (-1,1,1), (-1,0,7), (1,0,7), (-2,0,2), (2,0,2), (-1,-1,10), (1,-1,10), (0,-2,5)]     # m1_a = (0,-1)
m2 = [(-1,1,1), (-1,-1,1), (0,-1,7), (0,1,7), (0,-2,2), (0,2,2), (1,-1,10), (1,1,10), (2,0,5)]      # m2_a = (1,0)
m3 = [(1,-1,1), (-1,-1,1), (-1,0,7), (1,0,7), (-2,0,2), (2,0,2), (1,1,10), (-1,1,10), (0,2,5)]      # m3_a = (0,1)
m4 = [(1,1,1), (1,-1,1), (0,-1,7), (0,1,7), (0,-2,2), (0,2,2), (-1,-1,10), (-1,1,10), (-2,0,5)]     # m4_a = (-1,0)

m = [m1, m2, m3, m4]

route = [start_point]
idx = 0
length = 1

flag = False

## 먼지 이동 값 저장 함수
def move_dust(x, y, idx):
    global ans
    selected_m = m[idx]     # 현재 방향에 해당되는 먼지 비율의 위치들
    selected_d = d[idx]     # 현재 방향에 해당되는 a%의 위치

    dust = matrix[x][y]
    moved_dust = 0

    # 먼지 비율대로 계산
    for j in range(len(selected_m)):
        sx = x + selected_m[j][0]
        sy = y + selected_m[j][1]
        n_dust = dust * selected_m[j][2] // 100
        if(check_range(sx, sy)):
            matrix[sx][sy] += n_dust    # 밖으로 안나가면 해당되는 matrix 위치 값에 더해주기
        else:
            ans += n_dust   # 밖으로 나간 먼지는 ans에 더해주기
        moved_dust += n_dust    # a값을 계산하기 위해 다른 격자에 이동한 먼지의 양은 모두 더해서 저장해두기

    # a%값 계산
    a = dust - moved_dust
    dx = x + selected_d[0]
    dy = y + selected_d[1]
    if (check_range(dx, dy)):
        matrix[dx][dy] += a
    else:
        ans += a

    matrix[x][y] = 0


## 토네이도 이동 -> 먼지 이동
while(True):
    if(flag):   # (0,0)에 도착한 flag면 종료
        break

    curr = route[-1]
    x = curr[0]
    y = curr[1]

    for i in range(length):
        nx = x + d[idx % 4][0]
        ny = y + d[idx % 4][1]

        route.append((nx, ny))          # 이동하는 토네이도 루트

        move_dust(nx, ny, idx % 4)      # 먼지 이동

        # 길이만큼 다음칸 이동하기 위해 업데이트
        x = nx
        y = ny

        # (0,0)에 도착하면 종료
        if (x == 0 and y == 0):
            flag = True
            break

    idx += 1

    if(idx % 2 == 0):   # 인덱스가 계속 늘어나면서 만약 2번 꺾었다면 -> 다음 이동되는 길이는 +1 늘어나기
        length += 1

print(ans)