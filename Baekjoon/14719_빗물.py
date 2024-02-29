H, W = map(int, input().split())
block_list = list(map(int, input().split()))

rain_map = [list(0 for _ in range(W)) for _ in range(H)]

# 블럭이 쌓인대로 0과 1로 rain_map 표기 (1 == 블럭이 있는 곳)
for b in range(len(block_list)):
    block = block_list[b]
    for j in range(H-1, -1, -1):
        if(block > 0):
            rain_map[j][b] = 1
            block -= 1
        else:
            break

# print(rain_map)

# 총 빗물 수를 담을 변수
ans = 0

# rain_map 에서 빗물이 고이는 곳 탐색
for i in range(H):
    # 각 행의 블럭 수 카운트
    n_block = []
    for j in range(W):
        if(rain_map[i][j] == 1):
            n_block.append([i, j])

    # 블럭이 2개 이상 -> 빗물이 고임
    rain_cnt = 0
    if(len(n_block) >= 2):
        for n in range(len(n_block)-1, -1, -1):
            if(n > 0):
                rain_cnt += n_block[n][1] - n_block[n-1][1] - 1

    ans += rain_cnt

print(ans)