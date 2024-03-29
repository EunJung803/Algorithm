def solution(n):
    ans = 1  # 0에서 1은 무조건 점프 한번 해야하므로 1은 더해놓고 시작

    # 점프는 최소화, 순간이동은 현재위치 * 2로 이동
    # 최소 건전지 사용량 리턴하기

    while (n > 1):
        if (n % 2 != 0):  # 홀수면 -> 점프로 1칸 이동
            ans += 1
            n -= 1
        n = n // 2  # 2로 계속 나눠주면서 이동

    return ans