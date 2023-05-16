# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의

N = int(input())
nums = list(map(int, input().split()))

def find_median(t):
    median_index = (N + 1) // 2
    ans = t[median_index - 1]
    return ans


median = find_median(sorted(nums))
print("%d" %median)
