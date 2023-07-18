from itertools import combinations


def solution(numbers):
    answer = []

    a = list(combinations(numbers, 2))      # numbers 배열에서 2개씩 뽑아서 만드는 조합

    for i in range(len(a)):
        numbers_sum = a[i][0] + a[i][1]     # 2개씩 뽑은 값의 합을 구한다.
        if (numbers_sum in answer):         # 만약 이미 있는 값이라면 넣지 않는다.
            continue
        else:
            answer.append(numbers_sum)

    answer.sort()       # 오름차순으로 정렬
    return answer