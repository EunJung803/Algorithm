def solution(land):
    global max_index
    answer = 0

    """
    | 1 | 2 | 3 | 5 |
    | 5 | 6 | 7 | 8 |
    | 4 | 3 | 2 | 1 |
    """

    # 같은 열을 계속 밟을 수 없음
    # 얻을 수 있는 점수의 최댓값 리턴
    # 행은 100,000 이하 자연수, 열은 4

    for i in range(1, len(land)):
        for j in range(4):      # 각 행의 열 중에서
            sub_arr = []
            for k in range(4):  # 자기보다 위에 있는 행의 값들을 다 더한걸 sub_arr 에 넣을 예정
                if (j != k):    # 만약 윗 행의 값들 중에 같은 열에 있는 값이라면 넣지 않아야함
                    sub_arr.append(land[i][j] + land[i - 1][k])
            land[i][j] = max(sub_arr)       # 자기자신과 같은 열에 있는 값을 제외하고 다 더했을 때, 가장 큰 값으로 골라주기

    answer = max(land[-1])

    return answer


if __name__ == '__main__':
    print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
    print(solution([[1, 1, 3, 1], [2, 3, 2, 2], [1, 4, 1, 1]]))     # 9
    print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))       # 20
    print(solution([[1, 2, 3, 4], [2, 3, 4, 100]]))     # 103
