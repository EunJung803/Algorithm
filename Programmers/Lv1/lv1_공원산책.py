def solution(park, routes):

    # Todo
    ## park 배열 -> S 위치 알아내기 (시작점)
    ## routes 문자열 쪼개기 -> 방향 배열 설정 -> N S W E 일 때 각각 row, column 이동 거리 설정
    ## 시작점에서 이동했을 때 -> park 배열 위치를 벗어난다면 -> 해당 route 사용 X (continue로 건너뛰기)
    ##                     park 배열 위치를 벗어나지 않는다면 -> 장애물을 만나는지 확인하기
    ## 이동 거리까지 한칸씩 이동했을 때 -> 장애물이 있다면 -> 해당 route 사용 X
    ## 장애물을 만나지 않는다면 -> 최종 이동해야하는 row, column 거리만큼 이동하기!

    current_location = []       # 현재 위치를 계속 갱신하며 담을 배열
    two_dim_park = []           # park 배열의 2차원 버젼을 담을 배열

    # park 배열에서 S 위치 알아내기 + 2차원 배열로 만들기
    for sub_park in park:
        sub_array = []
        for i in range(len(sub_park)):
            sub_array.append(sub_park[i])

            if(sub_park[i] == "S"):
                current_location.append(park.index(sub_park))
                current_location.append(i)

        two_dim_park.append(sub_array)

    r, c = 0, 0     # 각 route 별 이동해야 할 row, column 거리를 담을 변수

    # routes 배열을 쪼개서 -> 각 route를 파악 -> 이동해야 할 row, column 거리 담기 -> park 밖으로 나가는지 and 장애물을 만나는지 검사 -> 모두 통과한다면 이동
    for i in range(len(routes)):

        op = routes[i].split(' ')[0]        # 방향
        n = int(routes[i].split(' ')[1])    # 거리

        cannot_go = False       # 장애물을 만나는지 따질 때 사용

        r_location = current_location[0]
        c_location = current_location[1]

        if (op == 'N'):
            r = -n
            c = 0

            # park 바깥까지 나간다면 -> continue로 건너뛰어서 이 route 사용하지 않기
            if (r_location + r >= len(two_dim_park) or c_location + c >= len(two_dim_park[0]) or
                    r_location + r < 0 or c_location + c < 0):
                continue

            # park 바깥에 나가지 않는다면 -> 장애물을 만나는지 확인
            for move in range(1, n+1):
                r_location = r_location - 1         # N은 북쪽으로 올라가는 방향이니까 -> row 위치가 n만큼 -1씩 변하게 됨
                if(two_dim_park[r_location][c_location] == 'X'):    # 장애물을 만난다면
                    cannot_go = True        # 지나갈 수 없음
                    break

            # 장애물도 만나지 않는다면 -> 이동하기
            if (cannot_go == False):
                current_location[0] = current_location[0] + r
                current_location[1] = current_location[1] + c


        if (op == 'S'):
            r = n
            c = 0

            if (r_location + r >= len(two_dim_park) or c_location + c >= len(two_dim_park[0]) or
                    r_location + r < 0 or c_location + c < 0):
                continue

            for move in range(1, n+1):
                r_location = r_location + 1         # S은 남쪽으로 내려가는 방향이니까 -> row 위치가 n만큼 +1씩 변하게 됨
                if(two_dim_park[r_location][c_location] == 'X'):
                    cannot_go = True
                    break

            if (cannot_go == False):
                current_location[0] = current_location[0] + r
                current_location[1] = current_location[1] + c


        if (op == 'W'):
            r = 0
            c = -n

            if (r_location + r >= len(two_dim_park) or c_location + c >= len(two_dim_park[0]) or
                    r_location + r < 0 or c_location + c < 0):
                continue

            for move in range(1, n+1):
                c_location = c_location - 1         # W은 왼쪽으로 이동하는 방향이니까 -> column 위치가 n만큼 -1씩 변하게 됨
                if (two_dim_park[r_location][c_location] == 'X'):
                    cannot_go = True
                    break

            if (cannot_go == False):
                current_location[0] = current_location[0] + r
                current_location[1] = current_location[1] + c


        if (op == 'E'):
            r = 0
            c = n

            if (r_location + r >= len(two_dim_park) or c_location + c >= len(two_dim_park[0]) or
                    r_location + r < 0 or c_location + c < 0):
                continue

            for move in range(1, n+1):
                c_location = c_location + 1         # E은 오른쪽으로 이동하는 방향이니까 -> column 위치가 n만큼 +1씩 변하게 됨
                if (two_dim_park[r_location][c_location] == 'X'):
                    cannot_go = True
                    break

            if (cannot_go == False):
                current_location[0] = current_location[0] + r
                current_location[1] = current_location[1] + c


    return current_location


if __name__ == '__main__':
    print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
    print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
    print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))
    print(solution(["OOO", "OSO", "OOO", "OOO"], ["N 2", "S 2"]))             # [3, 1]
    print(solution(["OOOS", "OOXX", "OOOO"], ["N 2", "W 1", "S 1", "S 2"]))   # [0, 2]
    print(solution(["OXOO", "OSOX", "OOOO"], ["N 1", "E 2", "S 1"]))          # [2, 1]


"""
N
r -1

S
r + 1

W
c - 1

E
c + 1


def check(r, c, current_location, two_dim_park, cannot_go):
    if (current_location[0] + r >= len(two_dim_park) or current_location[1] + c >= len(two_dim_park[0]) or
            current_location[0] + r < 0 or current_location[1] + c < 0):
        continue

    r_location = current_location[0]
    c_location = current_location[1]
    for move in range(1, n + 1):
        r_location = r_location - 1
        if (two_dim_park[r_location][c_location] == 'X'):
            cannot_go = True
            break

    if (cannot_go == False):
        current_location[0] = current_location[0] + r
        current_location[1] = current_location[1] + c

 # 현재 이동한 거리가 공원 범위 밖이라면 갈 수 없음
        # if (current_location[0] >= len(two_dim_park) or current_location[1] >= len(two_dim_park[0]) or current_location[0] < 0 or current_location[1] < 0):
        #     current_location[0] = current_location[0] - r
        #     current_location[1] = current_location[1] - c

        # 장애물이 있다면 갈 수 없음 -> 현재 이동한 거리가 장애물 이거나 or 장애물이 이동하려는 거리 안에 있다면
        # if (two_dim_park[current_location[0]][current_location[1]] == 'X'):
        #     current_location[0] = current_location[0] - r
        #     current_location[1] = current_location[1] - c

        # check_obstacle(current_location, x_location)

        # for x in x_location:
        #     if (current_location[0] >= x[0] and current_location[1] >= x[1]):       ## Todo : 여기 수정해야함
        #         current_location[0] = current_location[0] - r
        #         current_location[1] = current_location[1] - c

    # print(current_location)
"""