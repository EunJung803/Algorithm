def solution(a, b, n):
    answer = 0

    while(n >= a):  # 교환할 콜라의 수가 교환해주는 기준 a보다 클때까지 반복
        new_cola = (n // a) * b     # 마트에서 교환해서 받는 새 콜라 수
        left_cola = n % a           # 남는 콜라 수 (만약 교환할 때 나누어 떨어지지 않으면 남게 되기 때문)

        answer += new_cola          # answer에 받은 콜라 더하기
        n = new_cola + left_cola    # n 갱신 (만약 콜라가 남았다면 더해줘서 다음에 마트갈 때 교환 시도)

    return answer


if __name__ == '__main__':
    print(solution(2, 1, 20))
    print(solution(3, 1, 20))