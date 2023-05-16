# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의

T = int(input())
# nums = list(map(int, input().split()))
nums = [list(map(int, input().split())) for _ in range(T)]  # int 여러줄 입력받기 (2차원 배열로 저장)

def sum_func(t):
    sum = 0
    for i in range(len(t)):
        if (t[i] % 2 != 0):
            sum += t[i]
    return sum


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(0, T):
    # ///////////////////////////////////////////////////////////////////////////////////
    sum = sum_func(nums[i])
    print("#%d %d" %(i+1, sum))
    # ///////////////////////////////////////////////////////////////////////////////////
