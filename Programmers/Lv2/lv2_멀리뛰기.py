def solution(n):
    if (n <= 3):
        return n

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1234567

    print(dp)
    return dp[n]

if __name__ == '__main__':
    print(solution(5))
    print(solution(6))
    print(solution(7))
    print(solution(8))

    # n = 1, result = 1
    # n = 2, result = 2
    # n = 3, result = 3
    # n = 4, result = 5
    # n = 5, result = 8
    # n = 6, result = 13
    # n = 7, result = 21
    # n = 8, result = 34