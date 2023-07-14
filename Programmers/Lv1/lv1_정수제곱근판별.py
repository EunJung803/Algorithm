import math

def solution(n):
    answer = -1

    if ((math.sqrt(n)).is_integer()):
        answer = int((math.sqrt(n) + 1) ** 2)

    return answer

print(solution(121))
print(solution(3))
