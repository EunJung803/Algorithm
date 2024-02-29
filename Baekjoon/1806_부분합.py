N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0

cal_sum = 0         # 수열의 부분합을 구할 변수
min_length = N      # 최소 길이를 담을 변수
flag = False        # 부분합을 만들 수 있는지 확인할 flag

# 투포인터로 누적합 구하기
for i in range(N):
    start = i
    while(cal_sum < S and end < N):     # start 인덱스부터 end를 늘려가며 범위 내의 누적합 구하기
        cal_sum += arr[end]
        end += 1
    # 누적합이 S를 넘어가고, 최소 길이를 만족한다면 -> min_length 갱신, 부분합 만들 수 있으므로 flag 체크
    if(cal_sum >= S and end - start <= min_length):
        min_length = end - start
        flag = True
    cal_sum -= arr[start]       # 다음 start 값 부터의 탐색을 위해서 현재 start 값은 빼주고 넘어가기

# 정답 출력
if(flag):
    print(min_length)
else:
    print(0)