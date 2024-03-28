from collections import deque

N, K = map(int, input().split())

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 걷기 : 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동 : 1초 후에 2*X의 위치로 이동하게 된다.

# def K_distance(loc):
#     return abs(K - loc)

q = deque()
visited = [0 for _ in range(51)]

q.append(N)

while (q):
    curr = q.popleft()
    cnt = visited[curr]

    if (curr == K):
        print(cnt)
        break

    walk_f = curr + 1       # walk forward
    walk_b = curr - 1       # walk back
    jump = curr * 2         # jump (순간이동)

    for i in (walk_f, walk_b, jump):
        if i >= 0 and i <= 50 and visited[i] == 0:
            visited[i] = cnt+1
            q.append(i)
            # print(i, visited)

    # print(visited)
    # if(visited[walk_f] == 0 and visited[walk_b] == 0 and visited[jump] == 0):
    #     if(abs(K - jump) > abs(K - walk_b) or abs(K - jump) > abs(K - walk_f)):
    #         if(abs(K - walk_b) > abs(K - walk_f)):
    #             q.append(walk_f)
    #             visited[walk_f] = 1
    #             print(walk_f)
    #         if(abs(K - walk_b) < abs(K - walk_f)):
    #             q.append(walk_b)
    #             visited[walk_b] = 1
    #             print(walk_b)
    #
    #     if (abs(K - jump) < abs(K - walk_b) and abs(K - jump) < abs(K - walk_f)):
    #         q.append(jump)
    #         visited[jump] = 1
    #         print(jump)

