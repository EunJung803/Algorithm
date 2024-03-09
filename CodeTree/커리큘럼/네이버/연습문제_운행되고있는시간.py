N = int(input())
work_hour = [list(map(int, input().split())) for _ in range(N)]

# ex) [1 4) [3 7) [5 9)
# 1 2 3 4 5 6 7 8 9
# [     ]
#     [       ]
#         [        ]

# 범위를 설정하기 위해 직원들 중 가장 마지막 시간의 길이 찾기
length = 0
for i in range(len(work_hour)):
    if(length < work_hour[i][0]):
        length = work_hour[i][0]
    if(length < work_hour[i][1]):
        length = work_hour[i][1]

max_cnt = 0
for i in range(N):
    to_fire = work_hour[i]      # 해고할 직원 하나 선정
    check = []
    for j in range(N):
        if (work_hour[j] != to_fire):       # 해고할 직원을 제외하고 시간 계산을 하기 위해 check 리스트에 담기
            check.append(work_hour[j])

    # 남은 직원들의 일하는 시간 표시
    check_time = [False for _ in range(length)]
    for i in range(len(check)):
        for j in range(check[i][0]-1, check[i][1]-1):   # 각 직원의 일하는 시간들 True로 칠하기
            check_time[j] = True

        # print(check_time)

    cnt = check_time.count(True)    # True면 직원이 일하고 있는 시간이므로 True들을 count
    if(max_cnt < cnt):      # 최대 운행 되고 있는 시간 찾기
        max_cnt = cnt

print(max_cnt)