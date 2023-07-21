def solution(d, budget):
    answer = 0

    d.sort()    # 최대로 많은 부서의 물품을 구매해야하므로 값이 적은거부터 우선적으로 지원한다면, 더 많이 지원 가능

    for i in range(len(d)):
        budget -= d[i]      # 예산에서 값을 하나씩 빼는데
        if(budget < 0):     # 음수가 나온다면 -> 더 이상 구매 불가
            break
        answer += 1         # 음수가 아니라면 -> 구매 가능하므로 answer += 1

    return answer

if __name__ == '__main__':
    print(solution([1,3,2,5,4], 9))
    print(solution([2,2,3,3], 10))