N, M = map(int, input().split())

tmp = []

visited = [0 for _ in range(M+1)]

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 DFS 조합으로 뽑기
def permu(num):
    if(len(tmp) == M):
        print(' '.join(map(str, tmp)))      # 바로 출력
        return

    for n in range(num, N+1):
        if(n not in tmp):
            tmp.append(n)
            permu(n+1)
            tmp.pop(-1)
    return

permu(1)