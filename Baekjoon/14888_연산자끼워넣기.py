# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
# 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하기

from itertools import permutations

n = int(input())    # 수의 개수
nums = list(map(int, input().split()))  # 연산을 진행할 숫자들
ops = list(map(int, input().split()))   # + - * / 개수

ans = list()    # 계산한 값을 담는 리스트

ops_list = ['+', '-', '*', '/']
ops_johap = []      # 연산자들의 개수만큼 각 연산자들을 순서대로 담을 리스트

for i in range(len(ops)):
    if (ops[i] == 0):
        continue
    for j in range(ops[i]):
        ops_johap.append(ops_list[i])

ops_johap_permutation = list(permutations(ops_johap, len(ops_johap)))   # 연산자들의 순서별 조합들

# 연산자 순서별로 나오는 결과 저장
max_total = -(10 ** 10)
min_total = 10 ** 10
for p in range(len(ops_johap_permutation)):
    ops_select = ops_johap_permutation[p]   # 선택된 연산자 조합

    # 연산식 만들어서 계산
    total = nums[0]
    for i in range(n - 1):
        if(ops_select[i] == '+'):
            total += nums[i+1]
        if (ops_select[i] == '-'):
            total -= nums[i+1]
        if (ops_select[i] == '*'):
            total = int(total * nums[i+1])
        if (ops_select[i] == '/'):
            total = int(total / nums[i+1])

    if(total < min_total):
        min_total = total
    if(total > max_total):
        max_total = total

### eval() 사용해서 계산하는 방법
# for p in range(len(ops_johap_permutation)):
#     ops_select = ops_johap_permutation[p]   # 선택된 연산자 조합
#     start = int(eval(str(nums[0]) + ops_select[0] + str(nums[1])))   # 시작값 (첫번째 연산자 계산)
#
#     # 연산식 만들어서 계산
#     total = start
#     for i in range(1, n - 1):
#         if (i < n-1):
#             # print(str(total) + ops_select[i] + str(nums[i+1]))
#             total = int(eval(str(total) + ops_select[i] + str(nums[i+1])))
#     if(total < min_total):
#         min_total = total
#     if(total > max_total):
#         max_total = total
#     # ans.append(total)

# 정답 출력
print(max_total)
print(min_total)
