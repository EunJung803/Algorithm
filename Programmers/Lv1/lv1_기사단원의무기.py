def get_yaksu_count(num):
    count = 0

    # for i in range(1, num+1):
    #     if(num % i == 0):
    #         count += 1

    for i in range(1, int(num ** (1 / 2)) + 1):
        if (num % i == 0):
            count += 1
            if ((i ** 2) != num):
                count += 1

    return count


def solution(number, limit, power):
    answer = 0

    yak_su = []
    for i in range(1, number + 1):
        count = get_yaksu_count(i)
        if (count > limit):
            count = power
        yak_su.append(count)

    answer = sum(yak_su)

    return answer