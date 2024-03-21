def solution(N, number):
    answer = -1

    if (N == number):
        return 1

    dp = []

    for cnt in range(1, 9):
        tmp = set()
        tmp.add(int(str(N) * cnt))      # N을 cnt번 붙이기
        print(tmp)

        for i in range(cnt-1):
            # dp에 저장되어있는 계산된 값들 중 하나씩 꺼내서 사칙연산 -> append
            for first in dp[i]:     # dp에 맨 앞의 set에서부터 하나씩 꺼내기 (== first, 바로 이전에 계산된 set은 제외)
                for second in dp[-i-1]:     # 바로 이전에 계산된 set에서 값 하나씩 꺼내기 (== second)
                    tmp.add(first + second)
                    tmp.add(first - second)
                    tmp.add(first * second)
                    if(second != 0):
                        tmp.add(first // second)

            if(number in tmp):
                return cnt

        dp.append(tmp)

    return answer


if __name__ == '__main__':
    print(solution(5, 12))
    print(solution(2, 11))


# 틀렸던 이전 코드 (N의 조합을 고려하지 못함, ex) 55, 555, ...)
"""
cnt = 2

if (N == number):
    return 1

dp = [[] for _ in range(9)]

dp[0] = [N, N, N, N]
dp[1] = [N + N, N - N, N / N, N * N]

for a in range(2, 9):
    if (a == 2):
        exp_list = dp[a - 1]

        for j in range(4):
            curr = exp_list[j]
            tmp = []

            tmp.append(int(curr + N))
            tmp.append(int(curr - N))
            tmp.append(int(curr // N))
            tmp.append(int(curr * N))

            # print(a, tmp)
            if (number in tmp):
                return a
            dp[a].append(tmp)

        continue

    else:
        for i in range(len(dp[a - 1])):
            exp_list = dp[a - 1][i]

            for j in range(4):
                curr = exp_list[j]
                tmp = []

                tmp.append(int(curr + N))
                tmp.append(int(curr - N))
                tmp.append(int(curr // N))
                tmp.append(int(curr * N))

                # print(a, tmp)
                if (number in tmp):
                    return a
                dp[a].append(tmp)
            continue

    # print(dp)

return answer
"""