N, M = map(int, input().split())

tmp = []

# 정답 복사해서 저장하기
result = []
def copy_list(arr):
    for i in range(len(arr)):
        result.append(arr[i])

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 DFS 조합으로 뽑기
def permu():
    if(len(tmp) == M):
        # copy_list(tmp)
        print(' '.join(map(str, tmp)))      # 바로 출력
        return

    for n in range(1, N+1):
        if(n not in tmp):
            tmp.append(n)
            permu()
            tmp.pop(-1)
    return

permu()

# # 정답 출력
# for i in range(0, len(result), M):
#     print(' '.join(map(str, result[i:i+M])))