N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

max_coin = 0

# 3*3 크기만큼 탐색하여 해당하는 값을 coin 리스트에 담는 함수
def get_coin(row_s, col_s, row_e, col_e):
    coin = []
    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            coin.append(matrix[row][col])
    return coin

# 모든 격자를 돌며 범위 내의 3*3 격자 찾아서 동전 카운트
for i in range(N):
    for j in range(N):

        if(i+2 >= N or j+2 >= N):
            continue

        coin_list = get_coin(i, j, i+2, j+2)
        curr_coin = coin_list.count(1)

        if(max_coin < curr_coin):
            max_coin = curr_coin

        # print(coin_list)

print(max_coin)