def solution(lottos, win_nums):
    answer = []

    zero_count = lottos.count(0)        # 0의 개수
    match_num = 0       # 민우가 구매한 로또 번호가 당첨 번호와 일치하는 개수

    lottos.sort()
    win_nums.sort()

    # 당첨번호와 구매한 로또 번호가 일치하는지 센다.
    for i in lottos:
        if(i == 0):
            continue
        else:
            if(i in win_nums):
                match_num += 1

    best_score = zero_count + match_num     # 최고 점수 = 0인 부분이 당첨번호라고 가정한다면, 일치한 번호 개수 + 0의 개수 가 최고 점수
    worst_score = match_num                 # 최저 점수 = 0인 부분은 모두 틀렸을 때, 일치한 번호 개수만이 최저 점수

    winning_place = [6, 5, 4, 3, 2]         # 일치한 번호 개수에 따른 순위를 정하기 위해 생성한 배열
                                            # (6개 일치 = 1등, 즉 이 배열에서 인덱스 + 1 한게 순위가 된다)

    # 최고 점수를 순위로 매기는 작업
    if(best_score in winning_place):
        answer.append(winning_place.index(best_score) + 1)
    else:
        answer.append(6)

    # 최저 점수를 순위로 매기는 작업
    if (worst_score in winning_place):
        answer.append(winning_place.index(worst_score) + 1)
    else:
        answer.append(6)

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))