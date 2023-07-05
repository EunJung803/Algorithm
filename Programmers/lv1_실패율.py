def solution(N, stages):
    answer = [] # 정답을 리턴할 리스트

    failed_total = []           # 각 스테이지의 실패율을 계산한 값을 저장할 리스트
    stage_arrive = len(stages)  # 스테이지에 도달한 플레이어 수
    count_player = 0            # 저번 스테이지에서 이미 계산해서 다음 스테이지에서는 고려하지 않아도 되는 플레이어 수 (시작은 0)

    dictionary = dict()         # 각 스테이지 번호를 실패율의 내림차순으로 정렬하기 위해 선언한 딕셔너리

    for i in range(1, N + 1):   # 각 스테이지에 대한 실패율 계산
        failed_player = []      # 해당 스테이지에 도달했으나 아직 클리어하지 못한 플레이어들을 담을 리스트
        for j in stages:        # 해당 스테이지에서 실패한 플레이어 찾아내기
            if (j == i):        # 해당 스테이지와 번호가 같다면 도달했으나 아직 클리어 못한 플레이어임
                failed_player.append(j)

        stage_arrive = stage_arrive - count_player      # 스테이지에 도달한 플레이어 수 갱신

        if(len(failed_player) == 0):      # 만약 스테이지에 도달한 유저가 없는 경우
            failed_total.append(0)  # 실패율은 0
        else:
            failed_total.append(len(failed_player) / stage_arrive)      # 실패율 계산 (스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수)
        count_player = len(failed_player)       # 다음 스테이지 실패율 계산을 위해 이번 실패율 계산에 사용된 플레이어 수를 미리 저장해두기

        dictionary[i] = failed_total[i-1]   # 딕셔너리에 추가 (key : 현재 스테이지 번호 i, value : 해당 스테이지의 실패율 값)

    # 모든 실패율 계산 이후
    ans_list = sorted(dictionary.items(), reverse=True, key=lambda item: item[1])   # 딕셔너리의 value값 (실패율) 기준으로 내림차순 정렬
    print(ans_list)

    # 정렬된 형태가 튜플로 묶여서 리스트에 들어가있기 때문에 스테이지 번호만 추출하기 진행
    for i in ans_list:
        answer.append(i[0])     # answer 리스트에 스테이지 번호만 걸러서 추가하기

    return answer

if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(4, [4,4,4,4,4]))
    print(solution(5, [2, 1, 2, 1]))