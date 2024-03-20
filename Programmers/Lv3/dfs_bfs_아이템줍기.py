from collections import deque

def check_range(x, y, max_length):
    if (x < 0 or y < 0 or x >= (max_length * 2) + 1 or y >= (max_length * 2) + 1):
        return False
    return True


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 가장 큰 크기의 좌표값 구하기 (만들 map의 크기 설정을 위해)
    max_idx = 0
    for i in range(len(rectangle)):
        for j in range(len(rectangle[i])):
            if (rectangle[i][j] >= max_idx):
                max_idx = rectangle[i][j]

    matrix = [list(0 for _ in range((max_idx * 2) + 1)) for _ in range((max_idx * 2) + 1)]

    # map 만들기
    for i in range(len(rectangle)):
        # 함수 그래프의 (x,y) 좌표는 2차원배열 인덱스에서 반대로 적용됨 (그래서 x -> y, y -> x로 표현)
        y1, x1, y2, x2 = rectangle[i][0], rectangle[i][1], rectangle[i][2], rectangle[i][3]
        # 좌표 2배로 확장
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x1 < x < x2 and y1 < y < y2):  # 사각형의 내부인 경우 == 2로 채우기
                    matrix[x][y] = 2
                if (matrix[x][y] != 2):  # 테두리인 경우 == 1로 표시
                    matrix[x][y] = 1

            ## BFS 탐색
    visited = [list(0 for _ in range((max_idx * 2) + 1)) for _ in range((max_idx * 2) + 1)]

    q = deque()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 얘네도 좌표 2배 해주고, (x,y) 반대로 넣어주기
    item = [itemY * 2, itemX * 2]
    character = [characterY * 2, characterX * 2]

    q.append([character[0], character[1], 0])
    visited[character[0]][character[1]] = 1

    while (q):
        curr = q.popleft()
        y = curr[0]
        x = curr[1]
        cnt = curr[2]

        if (y == item[0] and x == item[1]):
            answer = cnt // 2
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (check_range(nx, ny, max_idx) and visited[ny][nx] == 0 and matrix[ny][nx] == 1):
                q.append([ny, nx, cnt + 1])
                visited[ny][nx] = cnt + 1

    return answer


if __name__ == '__main__':
    print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
    print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
    print(solution([[2, 1, 3, 6], [4, 1, 5, 6], [1, 2, 6, 3], [1, 4, 6, 5]], 3, 2, 5, 4))   # 8
    print(solution([[1, 1, 4, 4], [2, 2, 5, 5], [3, 3, 7, 8]], 1, 1, 5, 3))     # 6
    print(solution([[1,1,3,7],[2,2,7,4],[4,3,6,6]] , 1 , 2, 6, 6 ))     # 13