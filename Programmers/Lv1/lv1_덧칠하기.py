def solution(n, m, section):
    answer = 0

    wall = [1 for _ in range(n)]    # n 구역의 벽 배열 (기본으로는 다 1)

    for s in section:       # 색을 다시 칠해야 하는 부분은 0 으로 지정
        wall[s - 1] = 0

    for i in range(len(wall)):
        if (wall[i] == 0):              # 벽을 둘러면서 0인 부분을 만나면 -> 다시 칠해야함
            for j in range(i, i + m):   # 해당 섹션부터 롤러 크기가 닿는 곳까지 하나씩 칠하기
                if(j >= len(wall)):     # 만약 롤러가 벽의 크기를 벗어나면 -> 그만 칠하기
                    break
                wall[j] = 1
            answer += 1         # 페인트칠 했으니 횟수에 +1

    return answer


if __name__ == '__main__':
    print(solution(8, 4, [2, 3, 6]))
    print(solution(5, 4, [1, 3]))
    print(solution(4, 1, [1, 2, 3, 4]))
    print(solution(4, 2, [3, 4]))           # 1
    print(solution(5, 2, [1, 2, 5]))        # 2
