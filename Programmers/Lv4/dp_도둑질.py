## 코드 ver2
"""
from collections import deque

def solution(money):
    answer = 0

    N = len(money)

    dp = []
    nearby = [[] for _ in range(N)]

    q = deque()

    for i in range(N):
        for j in range(N):
            if (i != j):
                if (j == (i + 1) % N or j == (i - 1) % N):
                    nearby[i].append(j)

    for i in range(N):
        visited = [0 for _ in range(N)]
        visited[i] = 1
        for j in range(N):
            tmp = []
            if (j in nearby[i]):
                visited[j] = 1
            if (i != j and j not in nearby[i] and visited[j] == 0):
                q.append(j)
                visited[j] = 1
                tmp.append(i)
                tmp.append(j)

                while (q):
                    curr = q.popleft()

                    for next_home in range(N):
                        if (next_home != i):
                            if (visited[(next_home + 1) % N] == 1 or visited[(next_home - 1) % N] == 1):
                                continue
                            elif (curr != next_home and next_home not in nearby[curr] and visited[next_home] == 0):
                                q.append(next_home)
                                visited[next_home] = 1
                                tmp.append(next_home)
            if (tmp):
                m = 0
                for t in range(len(tmp)):
                    m += money[tmp[t]]
                dp.append(m)

    answer = max(dp)
"""
## 코드 ver 1
"""
    for i in range(N):
        tmp = []
        visited = [0 for _ in range(N)]

        current_idx = i

        if(visited[i] == 0):    # i = 0 -> 인접 = 1, 3
            visited[i] = 1
            for j in range(N):  # 0 1 2 3
                if(j != i):
                    if((j != (i+1)%N and j != (i-1)%N) and
                    visited[(i+1)%N] == 0 and (visited[(i-1)%N] == 0)):   # 인접한 집이 아닌 곳
                        # tmp.append(money[j])
                        visited[j] = 1
                        print(visited, j)
                        print((i+1)%N, (i-1)%N)
                        # i = j
        print("--")
        for j in range(N):
            if(visited[j] == 1):
                tmp.append(money[j])
        dp.append(tmp)

    print(dp)

    max_sum = 0
    for i in range(len(dp)):
        if(max_sum <= sum(dp[i])):
            max_sum = sum(dp[i])

    answer = max_sum


    return answer
    """

def solution(money):
    dp = [0 for _ in range(len(money))]     # n번째 집까지 털었을 때 최댓값을 각 인덱스 n에 저장

    # 첫 번째 집을 털 경우
    dp[0] = money[0]
    dp[1] = dp[0]
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])    # (현재 집 안털고 1칸 전의 집 털기) vs (현재 집 털기 + 2칸 전의 집 털기)

    tmp = max(dp)

    # 첫 번째 집을 털지 않을 경우
    dp = [0 for _ in range(len(money))]
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])

    return max(tmp, max(dp))


print(solution([1, 1, 1, 1, 2]))
# print(solution([1,2,3,1]), 4)
# print(solution([1,1,4,1,4]), 8)
# print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
# print(solution([1000,1,0,1,2,1000,0]), 2001)
# print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
# print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
# print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
# print(solution([11,0,2,5,100,100,85,1]), 198)
# print(solution([1,2,3]), 3)
# print(solution([91,90,5,7,5,7]), 104)
# print(solution([90,0,0,95,1,1]), 185)