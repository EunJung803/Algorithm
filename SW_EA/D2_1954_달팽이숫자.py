T = int(input())

# row, col 인덱스로 탐색할 수 있게 방향 설정 (오른쪽 -> 아래 -> 왼쪽 -> 위)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for t in range(1, T+1):
    N = int(input())    # 만들어질 배열의 크기

    snail = [[0] * N for _ in range(N)]     # 달팽이 배열의 크기 설정 (N * N)

    r, c = 0, 0     # 달팽이 배열에 값을 채워넣기 위한 인덱스를 담을 변수 (현재 위치)
    dist = 0        # dr, dc의 인덱스를 담을 변수 (0 : 오른쪽 / 1 : 아래 / 2 : 왼쪽 / 3 : 위)
    num = 1         # 현재 숫자

    while(num <= N*N):
        snail[r][c] = num
        num += 1

        r += dr[dist]
        c += dc[dist]

        if(r >= N or c >= N or r < 0 or c < 0 or snail[r][c] != 0):     # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있으면 방향 전환
            # 인덱스 재설정을 위해 실행 취소
            r -= dr[dist]
            c -= dc[dist]

            # 방향 전환
            dist = (dist + 1) % 4

            # 다시 수행
            r += dr[dist]
            c += dc[dist]

    print("#{}".format(t))
    for i in range(N):
        print(' '.join(map(str, snail[i])))