n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

happy = 0

# 행복한 수열인지 확인하는 함수
def check_happy(arr):
    max_cnt = 1
    cnt = 1
    for k in range(len(arr)-1):
        if(arr[k] == arr[k+1]):
            cnt += 1
        elif(arr[k] != arr[k+1]):     # 연속하여 동일한 원소가 나오지 않고 끊긴 구간에서 최대로 동일한 원소가 나온 횟수 업데이트
            if (max_cnt < cnt):
                max_cnt = cnt
            cnt = 1
    if (max_cnt < cnt):     # 한번 더 확인해서 최대 카운트로 업데이트
        max_cnt = cnt
    if(max_cnt >= m):
        return True
    else:
        return False

# 각 행, 각 열 담기
for i in range(n):
    sub1 = []
    sub2 = []
    for j in range(n):
        if(len(sub1) <= n):
            sub1.append(matrix[i][j])       # 행
        if(len(sub2) <= n):
            sub2.append((matrix[j][i]))     # 열

    # print(sub1)
    # print(sub2)

    # 행복한 수열인지 확인
    ck_1 = check_happy(sub1)
    ck_2 = check_happy(sub2)

    # 행복한 수열이라면 정답에 +1
    if(ck_1):
        happy += 1
    if(ck_2):
        happy += 1

    # print(happy)
    # print("==")

print(happy)