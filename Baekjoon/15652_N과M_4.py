N, M = map(int, input().split())

tmp = []
answer = []

def permu(num):
    if(len(tmp) == M):
        print(' '.join(map(str, tmp)))
        return

    for i in range(num, N+1):
        tmp.append(i)
        permu(i)
        tmp.pop()
    return

permu(1)

