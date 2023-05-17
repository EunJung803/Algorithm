from collections import Counter

T = int(input())
for t in range(0, T):
    N = int(input())    # 테스트케이스 번호
    score_arr = list(map(int, input().split()))     # 점수를 저장할 배열

    mode = (Counter(score_arr)).most_common()   # 최빈값 구하기 -> 내람차순 정리
    max_mode = mode[0][0]   # 최종 최빈값

    print("#%d %d" %(N, max_mode))