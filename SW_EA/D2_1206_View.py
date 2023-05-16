# 1206. [S/W 문제해결 기본] 1일차 - View
'''
2개씩 묶어서 비교
i는 2부터 시작 (인덱스)
i-2 i-1 <i> i+1 i+2

i를 기준으로 양옆 2개씩 비교
(i가 i-1보다 크고 and i-2보다 크고) and (i가 i+1보다 크고 and i+2보다 크면)
-> 조망권 확보 !
-> 몇개? => i - (i-2, i-1, i+1, i+2 중에서 제일 큰 수) 만큼 확보
'''

def max_height(before2, before1, after2, after1):
    arr = [before2, before1, after2, after1]
    max_val = before2
    for arr_val in arr:
        if(arr_val > max_val):
            max_val = arr_val
    return max_val

for t in range(0, 1):
    N = int(input())
    buildings = list(map(int, input().split()))

    jomang_count = 0

    for i in range(2, N-2, 1):
        if (buildings[i] > buildings[i-2] and buildings[i] > buildings[i-1]) and (buildings[i] > buildings[i+2] and buildings[i] > buildings[i+1]):
            sub_max_building = max_height(buildings[i-2], buildings[i-1], buildings[i+2], buildings[i+1])
            jomang_count += buildings[i] - sub_max_building

    print("#%ld %ld" % (t + 1, jomang_count))