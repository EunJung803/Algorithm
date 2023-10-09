def solution(sequence, k):
    answer = [0, 0]

    # 연속되는 부분 수열의 합이 k -> 그 중 길이가 제일 짧은 것의 [시작, 끝] 인덱스를 담아 리턴하기

    start = 0   # 시작 인덱스 (포인터)
    end = 0     # 끝 인덱스 (포인터)
    sum_s = 0   # 더한 값
    gap = len(sequence)     # 시작 인덱스와 마지막 인덱스의 거리 (제일 거리가 짧은 것이 정답이기에 필요)

    while(start < len(sequence)):   # 시작 인덱스를 가르키는 포인터가 배열의 끝에 도달할 때까지 while문 수행
        # 합이 k보다 작거나 같은 경우
        if(sum_s <= k):
            if (sum_s == k and end-start-1 < gap):      # k보다 같고, 기존 거리보다 더 짧은 거리를 가지는 인덱스들이라면 -> 정답으로 업데이트
                answer[0] = start
                answer[1] = end - 1
                gap = end-start-1
            # 배열의 마지막까지 도달했을 때 end값에 의한 인덱스 에러 방지용
            if(end < len(sequence)):        # end값이 배열 내의 인덱스라면 -> 계속 진행
                sum_s += sequence[end]      # end값을 빼주고 이동
                end += 1
            else:       # end값이 배열 밖의 인덱스라면 -> 탈출
                break

        # 합이 k보다 큰 경우
        else:
            sum_s -= sequence[start]    # start값을 빼주고 이동
            start += 1

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 2, 3, 4, 5], 5))