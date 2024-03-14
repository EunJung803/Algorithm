"""
# 이전 풀이
def solution(brown, yellow):
    answer = []

    # 갈색은 노란색을 다 감싸는 모양, 가로 >= 세로
    # a * b = 노란색 격자 수 라면 -> 갈색은 (a * 2) + (b * 2) + 4

    for i in range(1, yellow + 1):
        if (yellow % i == 0):
            yellow_r = i
            yellow_c = yellow // i
        if (((yellow_r * 2) + (yellow_c * 2) + 4) == brown):
            answer.append(max(yellow_r + 2, yellow_c + 2))
            answer.append(min(yellow_r + 2, yellow_c + 2))
            break

    return answer
"""

# 240314 풀이
def solution(brown, yellow):
    answer = []

    # (b_row-2) * (b_col-2) = y

    for b_row in range(1, brown + 1):
        b_col = (brown - (b_row * 2)) // 2 + 2

        if (b_row >= b_col):
            if ((b_row - 2) * (b_col - 2) == yellow):
                answer.append(b_row)
                answer.append(b_col)
                break

    return answer

if __name__ == '__main__':
    print(solution(10, 2))