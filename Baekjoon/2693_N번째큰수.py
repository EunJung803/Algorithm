T = int(input())
ans = []

for t in range(T):
    input_array = list(map(int, input().split()))

    sorted_array = sorted(input_array)
    ans.append(sorted_array[-3])

for i in range(T):
    print(ans[i])