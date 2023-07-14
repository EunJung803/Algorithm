def solution(price, money, count):
    answer = -1

    sum = 0
    for i in range(1, count + 1):
        sum += price * i

    if (money >= sum):
        answer = 0
    else:
        answer = abs(money - sum)

    return answer

if __name__ == '__main__':
    print(solution(3, 20, 4))