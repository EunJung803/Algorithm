def solution(left, right):
    answer = 0

    ## 약수를 다 찾고 -> 약수의 개수를 알아내고 -> 홀수인지 짝수인지 구별 -> 합할지 더할지 계산
    start = left
    for i in range(0, right - left + 1):

        # 약수들 다 찾아내기
        yak_su = []
        for j in range(1, start + 1):
            if (start % j == 0):
                yak_su.append(j)

        # 약수의 개수가 홀수인지 짝수인지
        if (len(yak_su) % 2 == 0):
            answer += start
        elif (len(yak_su) % 2 != 0):
            answer -= start

        # 다음 수도 검사하기
        start += 1

    return answer