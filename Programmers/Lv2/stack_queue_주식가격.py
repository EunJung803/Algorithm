def solution(prices):
    answer = []

    # 초 단위로 기록된 주식가격 -> 가격이 떨어지지 않은 기간이 몇초인지

    for i in range(len(prices)):
        check = True
        for j in range(i + 1, len(prices)):  # 현재 가격 기준으로 떨어진 가격이 있는지 확인하기
            if (prices[j] < prices[i]):  # 가격이 현재 가격보다 떨어졌다면
                ans_time = j - i  # 몇초인지 기간 구하기
                answer.append(ans_time)
                check = False
                break
        if (check):  # 현재 가격에서 떨어진게 그 뒤로 없다면,
            answer.append(len(prices) - 1 - i)  # 한번도 떨어지지 않음! 몇초인지 기간 구하기

    return answer