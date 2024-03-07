N, M = map(int, input().split())
seq_A = list(map(int, input().split()))
seq_B = list(map(int, input().split()))

cnt = 0

for i in range(N):
    flag = True
    sub_str = []
    for j in range(i, i+M):     # M개의 원소로 이루어진 부분 수열을 sub_str에 담기
        if(i+M <= N):
            sub_str.append(seq_A[j])
    if(sub_str):
        if(sorted(sub_str) == sorted(seq_B)):       # 정렬해서 비교했을 때, 수열 B과 동일하면 아름다운 수열
            cnt += 1

print(cnt)


## 메모리초과 난 코드
# from itertools import permutations
#
# N, M = map(int, input().split())
# seq_A = list(map(int, input().split()))
# seq_B = list(map(int, input().split()))
#
# cnt = 0
#
# beautiful_seq = list(permutations(seq_B))
#
# for i in range(N):
#     flag = True
#     sub_str = []
#     for j in range(i, i+M):
#         if(i+M <= N):
#             sub_str.append(seq_A[j])
#
#     if(tuple(sub_str) in beautiful_seq):
#         cnt += 1
#
# print(cnt)