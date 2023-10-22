# 1이상 ~ K이하 숫자를 하나 고르기 -> N번 반복하여 나오는 순서쌍 구하기

# K, N = map(int, input().split())
K, N = 2, 2

answer = []

def pick_num(num):  # 지금까지 num개의 숫자를 뽑았을 때 그 다음 어떤 수를 뽑을지 선택
    # 종료 조건
    if (num == N):  # N만큼 뽑았다면 탈출
        print(*answer)
        return

    # 실행 조건
    for i in range(1, K+1):     # K 이하의 수 중 그 다음 수를 append
        answer.append(i)
        pick_num(num + 1)
        answer.pop()

    return


pick_num(0)