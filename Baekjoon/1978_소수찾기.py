n = int(input())  # 수의 개수 N
nums = list(map(int, input().split()))  # 1000 이하의 자연수 N개

counts = []


def is_prime_num(x, counts):    # 소수인지 판별해야 하는 수 x
    prime_count = 0
    if(x <= 1):     # 1 이하면 소수 아님 (음수 포함)
        return 0
    for i in range(2, x):   # 2부터 x까지 나눠보기
        if (x % i == 0):    # 만약 2부터 x까지의 수인 i로 나눴을 때 나누어떨어지면 x는 소수가 아님
            return 0
        else:    # 나누어떨어지지 않으면 일단 오키 패스하자
            pass

    # 다 돌고나서 모든게 나누어떨어지지 않아서 여기까지 살아남은 수면 소수임 !
    prime_count += 1
    counts.append(prime_count)
    return counts

for i in range(n):    # 입력받는 수의 개수 n만큼 돌려보기
    is_prime_num(nums[i], counts)

ans = 0
for i in counts:    # 최종 입력받은 수들 중 판별된 소수의 갯수 카운트
    ans += i
print(ans)