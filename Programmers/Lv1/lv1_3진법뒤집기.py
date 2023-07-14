def solution(n):
    answer = 0

    # 3진법으로 변형하기
    samzinbup = []
    while (n > 0):
        div = n // 3        # 3으로 나눈 몫
        left = n % 3        # 3으로 나눈 나머지
        samzinbup.append(left)      # 나머지를 넣어주고
        n = div             # 몫을 3으로 다시 나누기위해 갱신

    # print(samzinbup)

    # 뒤집기
    sam_n = []
    for i in range(len(samzinbup) - 1, -1, -1):
        sam_n.append(samzinbup[i])

    # print(sam_n)

    # 10진법으로 계산하기
    for i in range(len(sam_n)):
        answer += sam_n[i] * (3 ** i)

    return answer

if __name__ == '__main__':
    print(solution(45))
    print(solution(125))
    print(solution(1))