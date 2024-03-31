N, M = map(int, input().split())

tmp = []

def permu():
    if(len(tmp) == M):
        print(' '.join(map(str, tmp)))
        return

    for i in range(1, N+1):
        tmp.append(i)
        permu()
        tmp.pop()
    return

permu()