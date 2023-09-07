def solution(triangle):
    answer = 0

    """
    << triangle >>
                    7 (0,0)
                3 (1,0) 8 (1,1)
            8 (2,0) 1 (2,1) 0 (2,2)
        2 (3,0) 7 (3,1) 4 (3,2) 4 (3,3)
    4 (4,0) 5 (4,1) 2 (4,2) 6 (4,3) 5 (4,4)
    
    << dp >>
                    7 (0,0)
                10 (1,0) 15 (1,1)
          18 (2,0) 11 vs 16 (2,1) 15 (2,2)
    y가
    0이면 -> x-1 인덱스에서 무조건 y가 0인 애가 더해짐
    1이면 -> x-1 인덱스에서 y가 0인거나 1인거 중에서 더했을 때 더 큰거
    2이면 -> x-1 인덱스에서 무조건 y가 1인 애가 더해짐 
    """
    # (x, y) 라고 하면 그 다음 y는 같은 y, y+1 인 곳으로 이동 가능

    dp = [[0 for j in range(len(triangle[i]))] for i in range(len(triangle))]

    dp[0][0] = triangle[0][0]

    # 각 좌표값 (x, y)
    for x in range(1, len(triangle)):
        for y in range(len(triangle[x])):
            if(x < 2):      # x가 1일땐 triangle[0][0]이 각자 자기자신과 더해지면 끝
                dp[x][y] = triangle[0][0] + triangle[x][y]
            else:
                # 밑에서 [x][y+1] 에 대한 값을 지정해주기 때문에 인덱스 에러가 나지 않기 위해 탈출문 설정
                if(y >= len(triangle[x])-1):
                    break
                dp[x][y] = max(dp[x][y], dp[x-1][y] + triangle[x][y])   # (현재 dp에 있는 값) vs (현재 dp의 위에 있는 값 + triangle의 현재 인덱스 값)
                dp[x][y+1] = dp[x-1][y] + triangle[x][y+1]              # 그 다음 비교를 위해 현재 dp 위에 있는 값을 미리 더해놓기

    answer = max(dp[-1])    # 더해진 마지막 최종 값들의 max가 정답

    return answer



if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))