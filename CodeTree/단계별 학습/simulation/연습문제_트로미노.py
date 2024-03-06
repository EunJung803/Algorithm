n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def check_range(x, y):
    if(x < 0 or y < 0 or x >= n or y >= m):
        return False
    return True

ans = []

# ㄴ 자 블럭
def block1(s1):
    # ㄴ , r (ㄱ자 반대) , ㄱ , ㅢ (ㄴ자 반대)
    dx = [[1, 1], [0, 1], [0, 1], [0, -1]]
    dy = [[0, 1], [1, 0], [1, 1], [1, 1]]

    # 블럭은 총 3개의 블럭으로 이루어짐
    ## 3개의 블럭 중 1번째 블럭
    x = s1[0]
    y = s1[1]
    total_block = []

    for i in range(4):
        b_sum = 0

        ## 3개의 블럭 중 2번째 블럭
        x1 = x + dx[i][0]
        y1 = y + dy[i][0]
        ## 3개의 블럭 중 3번째 블럭
        x2 = x + dx[i][1]
        y2 = y + dy[i][1]

        if(check_range(x1, y1) and check_range(x2, y2)):        # 블럭이 좌표 안에 존재할 수 있다면 -> 합 구해서 리스트에 넣어주기
            b_sum += matrix[x][y]
            b_sum += matrix[x1][y1]
            b_sum += matrix[x2][y2]
            total_block.append(b_sum)

    return total_block

# ㅣ 자 블럭
def block2(s2):
    # ㅡ , ㅣ
    dx = [[0, 0], [1, 2]]
    dy = [[1, 2], [0, 0]]

    # 블럭은 총 3개의 블럭으로 이루어짐
    ## 3개의 블럭 중 1번째 블럭
    x = s2[0]
    y = s2[1]
    total_block = []

    for i in range(2):
        b_sum = 0
        ## 3개의 블럭 중 2번째 블럭
        x1 = x + dx[i][0]
        y1 = y + dy[i][0]
        ## 3개의 블럭 중 3번째 블럭
        x2 = x + dx[i][1]
        y2 = y + dy[i][1]

        if (check_range(x1, y1) and check_range(x2, y2)):       # 블럭이 좌표 안에 존재할 수 있다면 -> 합 구해서 리스트에 넣어주기
            b_sum += matrix[x][y]
            b_sum += matrix[x1][y1]
            b_sum += matrix[x2][y2]
            total_block.append(b_sum)

    return total_block

for i in range(n):
    for j in range(m):

        s = [i, j]
        b1_sum = block1(s)
        b2_sum = block2(s)

        for b in range(len(b1_sum)):
            ans.append(b1_sum[b])
        for b in range(len(b2_sum)):
            ans.append(b2_sum[b])

# print(ans)
print(max(ans))
