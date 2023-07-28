def solution(name, yearning, photo):
    answer = []

    # yearning 점수의 합산 = 추억 점수

    for i in range(len(photo)):
        yearn_sum = 0
        for yearn_name in name:
            if(yearn_name in photo[i]):
                yearn_sum += yearning[name.index(yearn_name)]
        answer.append(yearn_sum)

    return answer