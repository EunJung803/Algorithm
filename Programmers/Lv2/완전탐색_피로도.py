from itertools import permutations


def solution(k, dungeons):
    answer = -1

    # 최소 필요 피로도 : 탐험을 위해 필요한 최소한의 피로도
    # 소모 피로도 : 탐험 후의 소모된 피로도
    # [최소 피로도, 소모 피로도]

    permu = [i for i in range(len(dungeons))]  # 방문할 순서
    cnt = 0

    p = list(permutations(permu))
    # print(p)

    for i in range(len(p)):
        cnt = 0
        curr_k = k
        seq = p[i]
        for j in range(len(seq)):
            curr_dungeon = dungeons[seq[j]]
            if (curr_k >= curr_dungeon[0]):
                curr_k -= curr_dungeon[1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)

    return answer

## DFS
# answer = 0
# N = 0
# visited = []
#
#
# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:
#         answer = cnt
#
#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0
#
#
# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#     return answer

if __name__ == '__main__':
    print(solution(80, [[80,20],[50,40],[30,10]]))