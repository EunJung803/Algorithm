def solution(n):
    answer = 0

    prime_nums = list()     # 찾은 소수를 담을 리스트

    ### 1. 절반으로 나눠서 나눠지는 수가 있으면 (약수 존재) -> 소수 아님 판별
    # for i in range(1, n + 1):
    #     check_sosu = True
    #     for j in range(2, (i//2)+1):
    #         if (j != i and i % j == 0):
    #             check_sosu = False
    #             break
    #     if (i != 1 and check_sosu):
    #         prime_nums.append(i)

    ### 2. 시간복잡도를 줄인 약수 구하기 버젼
    # for i in range(2, n + 1):
    #     check_sosu = True
    #     for j in range(2, int(i ** (1 / 2)) + 1):
    #         if (i % j == 0):
    #             check_sosu = False
    #             break
    #     if(check_sosu):
    #         prime_nums.append(i)

    ### 3. 에라토스테너스의 체 사용하기
    a = [0, 0] + [1] * (n - 1)  # 0부터 n까지 소수판별을 위해 사용할 리스트 (0과 1은 소수에서 제외되므로 0으로 설정, 2부터 n까지는 1로 설정)

    for i in range(2, n + 1):
        if (a[i] == 1):  # 1을 만나면 -> 소수
            # prime_nums.append(i)
            answer += 1
            for j in range(2 * i, n + 1, i):  # i가 소수면 -> i의 배수들은 소수에서 제외됨 (약수로 i를 갖기 때문에)
                a[j] = 0  # i의 배수들을 0으로 설정 (소수 X)

    return answer

if __name__ == '__main__':
    print(solution(10))
    print(solution(5))
    print(solution(3))
    print(solution(2))
    print(solution(100))        # 25
    print(solution(100000))     # 9592