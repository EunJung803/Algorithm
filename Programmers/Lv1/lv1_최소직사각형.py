def solution(sizes):
    answer = 0

    # 가로 중 최대값 x 세로 중 최대값 이 제일 작은거 구하기
    # 가로 세로 서로 교체 가능

    width = []
    height = []
    # 가로 vs 세로 중 둘 중 작은 수를 우선 가로에 다 배치
    for i in sizes:
        if (i[0] > i[1]):
            i[0], i[1] = i[1], i[0]
        width.append(i[0])
        height.append(i[1])

    # 가로의 최대 x 세로의 최대 구하기
    answer = max(width) * max(height)

    return answer