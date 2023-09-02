def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max((i // n), (i % n)) + 1)

    # left부터 right까지 판단
    # 0,2 -> 1,0 -> 1,1 -> 1,2
    # n = 3
    # 2//3 = 0...2 , 3//3 = 1...0, 4//3 = 1...1, 5//3 = 1...2

    return answer

# def solution(n, left, right):
#     answer = []
#
#     # 1) n*n 배열 만들기
#     # 2) i행 i열을 i로 채우기 (i는 1부터 n까지)
#     # 3) 행을 잘라서 이어붙이기
#     # 4) left:right 까지 슬라이싱
#     # -> 백퍼 시간초과 !
#
#     dim_n = [[0 for _ in range(n)] for _ in range(n)]
#
#     count_index = 0
#     for i in range(len(dim_n)):
#         for j in range(len(dim_n)):
#             dim_n[i][j] = max(i, j) + 1
#             answer.append(dim_n[i][j])
#
#             if (count_index == right):
#                 answer = answer[left:right + 1]
#                 break
#
#             count_index += 1
#
#     return answer