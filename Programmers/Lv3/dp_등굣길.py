def solution(m, n, puddles):
    answer = 0

    matrix = [list(0 for _ in range(m)) for _ in range(n)]
    dp = [list(0 for _ in range(m)) for _ in range(n)]

    # 물에 잠긴 지역 표시
    for i in range(len(puddles)):
        matrix[puddles[i][1] - 1][puddles[i][0] - 1] = 1

    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            # 시작 지점이 아니고, 물에 잠긴 지역이 아니면 -> 이전 이동해온 곳의 경우의 수 더해주기
            if not ((i == 0 and j == 0) or matrix[i][j] == 1):
                dp[i][j] += dp[i - 1][j]
                dp[i][j] += dp[i][j - 1]

        # for a in range(len(dp)):
        #     print(dp[a])
        # print("==")

    answer = dp[-1][-1] % 1000000007

    return answer