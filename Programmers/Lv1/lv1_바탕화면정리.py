def solution(wallpaper):
    answer = []

    # '.' == 빈칸 / '#' == 파일
    # wallpaper의 모든 원소의 길이는 동일
    # 파일을 모두 포함하면서, 최소한의 이동거리
    # 시작점 == S(lux, luy) / 끝점 == E(rdx, rdy) 의 최소 거리

    lux = len(wallpaper)
    luy = len(wallpaper[0])

    rdx = 0
    rdy = 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if(wallpaper[i][j] == "#"):
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)

    answer = [lux, luy, rdx, rdy]

    return answer

if __name__ == '__main__':
    print(solution([".#...", "..#..", "...#."]))
    print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
    print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
    print(solution(["..", "#."]))
    print(solution(["...", "...", "...", "...", "..#"]))        # [4, 2, 5, 3]