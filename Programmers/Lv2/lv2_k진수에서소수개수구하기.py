import math

# n을 k 진수로 변환하는 함수
def get_num(n, k):
    num = ''
    while n > 0:
        n, mod = divmod(n, k)
        num += str(mod)
    return num[::-1]

# 소수인지 확인하는 함수
def check_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    #
    # if (num < 2):
    #     return False
    # if (num >= 2):
    #     for i in range(2, num):
    #         if (num % i == 0):
    #             return False
    #     return True


def solution(n, k):
    answer = 0

    # k 진수 변환 -> 조건에 맞는 소수 개수 구하기

    # k 진수 변환
    num = get_num(n, k)
    print(num)

    # 조건에 맞는 소수 확인
    num_check = num.split("0")
    for i in range(len(num_check)):
        if(num_check[i] != '' and check_prime(int(num_check[i]))):
            answer += 1

    # zero_idx = 0
    # for i in range(len(num)):
    #     # P0 인 경우
    #     if (zero_idx == 0 and num[i] == '0'):
    #         zero_idx = i
    #         if (check_prime(int(num[:i]))):
    #             answer += 1
    #     # 0P0 인 경우
    #     elif (zero_idx != 0 and num[i] == '0'):
    #         if (check_prime(int(num[zero_idx:i]))):
    #             answer += 1
    #         zero_idx = i
    #     # 0P 인 경우
    #     elif (zero_idx != 0 and i + 1 == len(num)):
    #         if (check_prime(int(num[zero_idx:]))):
    #             answer += 1
    #     # p 인 경우
    #     elif (zero_idx == 0 and i + 1 == len(num)):
    #         if (check_prime(int(num[:]))):
    #             answer += 1

    return answer

if __name__ == '__main__':
    print(solution(110011, 10))