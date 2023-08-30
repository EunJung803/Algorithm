def solution(n):
    answer = 1      # 자기자신이 하나의 정답이 되므로 우선 answer는 1로 시작

    for i in range(1, (n // 2) + 1):    # 자신보다 절반 이상의 수부터는 연속적으로 더했을 때 자기자신이 나올수 없기 때문에 (n//2)+1 까지만 돌리기
        result = 0
        for j in range(i, (n // 2) + 2):    # 절반 그 다음까지 더해지는 경우를 위해 (n//2)+2 까지 돌리기
            result += j
            if (result > n):    # 더해서 만약 자기자신보다 커지면 정답 X
                break
            if (result == n):   # 자기자신이랑 같은 값이 나오면 answer + 1, 다음 수를 따지기 위해 break
                answer += 1
                break

    return answer