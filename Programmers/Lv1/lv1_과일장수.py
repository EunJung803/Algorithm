def solution(k, m, score):
    answer = 0

    # 한 상자에 m개씩 포장 -> 최저점(p) * m 이 한상자 가격
    # k가 최고점

    box = [0 for _ in range(m)]
    # print(box)

    score.sort(reverse=True)
    # print(score)

    b = 0
    for i in range(len(score)):
        box[b] = score[i]
        b += 1
        if (b % m == 0):
            answer += min(box) * m
            b = 0

    return answer


if __name__ == '__main__':
    print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
    print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
