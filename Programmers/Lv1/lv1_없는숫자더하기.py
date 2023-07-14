def solution(numbers):
    answer = -1

    num_sum = 0
    for i in numbers:
        num_sum += i

    answer = 45 - num_sum

    return answer