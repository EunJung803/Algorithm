### ver 1
def solution(money):
    answer = []

    change_left = money
    n = 1

    while (change_left >= 5500):
        change_left -= 5500
        if (change_left >= 5500):
            n += 1
            continue
        else:
            break

    answer.append(n)
    answer.append(change_left)

    return answer

### ver 2
# def solution(money):
#     answer = [money // 5500, money % 5500]
#     return answer

if __name__ == '__main__':
    solution(5500)
    solution(15000)