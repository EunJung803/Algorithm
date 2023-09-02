def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    # B에서 제일 큰 수가 A에서 제일 작은 수와 곱해지는 경우가 최적의 최솟값을 구하게 된다

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer


if __name__ == '__main__':
    print(solution([1, 4, 2], [5, 4, 4]))
    print(solution([1, 2], [3, 4]))

# from itertools import product
#
# def solution(A, B):
#     answer = 0
#
#     product_AB = list(product(A, B))
#     ans_list = []
#
#     for i in range(len(A)):
#         sum_ab = 0
#         sub_list = product_AB[i::len(A) + 1]
#         for j in range(len(sub_list)):
#             sum_ab += sub_list[j][0] * sub_list[j][1]
#         ans_list.append(sum_ab)
#
#     answer = min(ans_list)
#
#     return answer
