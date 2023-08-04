def solution(k, tangerine):
    answer = 0

    tangerine = sorted(tangerine)
    tan_dict = dict()

    # 딕셔너리 채우기
    for i in tangerine:
        if(tan_dict.get(i) == None):
            tan_dict[i] = 0
        tan_dict[i] += 1

    tan_dict_sorted = sorted(tan_dict.values(), reverse=True)   # 귤의 개수를 기준으로 내림차순 정렬하기
    print(tan_dict_sorted)

    for t in tan_dict_sorted:
        if (k <= 0):
            break
        k -= t
        answer += 1

    return answer


if __name__ == '__main__':
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
    print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
    print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
