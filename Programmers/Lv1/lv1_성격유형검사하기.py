# 1번 리스트를 만들어주는 함수
def make_survey_score(disagree, agree, choice_score_list):
    for i in range(3, 0, -1):
        choice_score_list.append([disagree, i])
    choice_score_list.append(["X", 0])
    for i in range(1, 4, 1):
        choice_score_list.append([agree, i])

    return choice_score_list

def solution(survey, choices):
    answer = ''

    # Todo
    ## 각 질문의 지표 별 비동의/동의 점수를 담을 list() 생성 - 1번 리스트
    ## 최종 점수를 기록할 list() 생성 - 2번 리스트    (ex. R T C F J M A N 순서대로 2차원 배열 형식, [성격 유형, 얻은 점수])
    ## survey를 하나씩 돌면서 지표 별 비동의/동의 1번 리스트에 기록   (ex. [['N', 3], ['N', 2], ['N', 1], ['X', 0], ['A', 1], ['A', 2], ['A', 3]]), 모르겠음 선택은 ['X', 0]
    ## choices번째에 있는 걸 1번 리스트에서 선택 -> 얻은 점수를 성격 유형에 따라 2번 리스트에 기록
    ## 다 돌면 2번 리스트 계산을 통해 각 지표 별 (2개씩 비교) 가장 점수가 높은 성격 유형 선택 -> 점수가 같은게 있으면 더 앞에 있는걸로 선택 -> 정답 완성

    final_score_dict = list()       # 2번 리스트
    personality = ["R", "T", "C", "F", "J", "M", "A", "N"]      # 사전 순으로 정리
    """
    R T
    C F
    J M
    A N
    """
    for i in range(8):      # 2번 리스트 만들기
        final_score_dict.append([personality[i], 0])

    # 각 문항 별 점수 계산하여 기록하기
    for n in range(len(survey)):
        disagree = survey[n][0]     # 비동의
        agree = survey[n][1]        # 동의

        choice_score_list = make_survey_score(disagree, agree, [])      # 1번 리스트 생성
        get_choice = choice_score_list[choices[n]-1][0]     # choices 값에 따라 선택된 성격 유형
        get_score = choice_score_list[choices[n]-1][1]      # choices 값에 따라 선택된 점수

        if(get_choice == "X"):  # 만약 모르겠음이 골라지면 -> 건너뛰기
            continue
        choice_index = personality.index(get_choice)        # 선택된 성격 유형의 사전별 인덱스
        final_score_dict[choice_index][1] += get_score      # 2번 리스트 중 해당 인덱스에 있는 값을 찾아서 -> 점수 업데이트

    # print(choice_score_list)
    # print(final_score_dict)

    # 2개씩 비교해서 각 지표별 얻은 성격유형 찾아내기 -> answer에 추가
    for i in range(0, len(final_score_dict), 2):
        if(final_score_dict[i][1] >= final_score_dict[i+1][1]):     # 같으면 사전순으로 빠른게 선택됨
            answer += final_score_dict[i][0]
        elif(final_score_dict[i][1] < final_score_dict[i+1][1]):
            answer += final_score_dict[i+1][0]

    return answer

if __name__ == '__main__':
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
    print(solution(["TR", "RT", "TR"], [7, 1, 3]))
    print(solution(["TR", "CF", "JM", "AN"], [4, 4, 4, 4]))         # RCJA
    print(solution(["NA", "NA", "NA"], [1, 1, 1]))                  # RCJN