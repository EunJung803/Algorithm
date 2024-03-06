n, t = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]

time = 0

while(time < t):
    # 두번째줄의 배열은 우선 반대로 돌려서 -> 원소들 이동 -> 마지막에 다시 돌리기
    tmp = belt[1]
    belt[1] = tmp[::-1]

    # 위치가 덮어써지므로 tmp로 저장해둘 원소들
    tmp1 = belt[1][0]
    tmp2 = belt[0][n-1]

    # 윗줄 덮어쓰기
    for x in range(n-1, 0, -1):
        belt[0][x] = belt[0][x-1]
    # 아랫줄 덮어쓰기
    for y in range(n-1):
        belt[1][y] = belt[1][y+1]

    # 저장된 원소들 이동시켜서 배치
    belt[0][0] = tmp1
    belt[1][n-1] = tmp2

    # 두번째줄의 배열 다시 돌리기
    tmp = belt[1]
    belt[1] = tmp[::-1]

    time += 1

# 정답 출력
for i in range(len(belt)):
    print(' '.join(map(str, belt[i])))
