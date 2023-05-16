# 입력
'''
T개의 테스트케이스
배열 len
배열
'''

T = int(input())
N = 0
for t in range(T):
    # 입력받기
    N = int(input())
    nums = list(map(int, input().split()))

    # 최대 이익 얻기
    # 제일 큰 매매가와 그 매매가의 인덱스 찾기 -> 최대 이익 계산
    max_element = nums[-1]  # 배열의 최대값
    max_index = -1          # 최대값이 위치한 인덱스
    max_profit = 0          # 최대 이익값 (출력할 정답)
    for i in range(N-2, -1, -1):    # 뒤에서부터 거꾸로 따져보기
        if (nums[i] >= max_element):    # 만약 최대값이 마지막 인덱스가 아니라 i번째 요소라면
            max_element = nums[i]       # 최대값 업데이트
            max_index = i
        else:       # 최대값이 i번째 요소가 아니라면 -> 현재 얻을 이익 계산하기
            profit = max_element - nums[i]  # 최대값 - 현재 매매가
            max_profit += profit            # 최대 이익값에 현재 얻을 수 있는 이익 더해서 업데이트

    # 첫쨋날이 제일 큰 매매가일 경우 -> 최대 이익은 없음
    if (max_index == 0):
        max_profit = 0

    print("#%ld %ld" % (t + 1, max_profit))

