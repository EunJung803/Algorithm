def solution(id_list, report, k):
    # 중복 제거 (한 유저가 같은 유저를 여러번 신고한 경우는 1회로 처리하기 위해)
    report = list(set(report))

    # 정답을 리턴할 answer 리스트 (id_list 만큼의 길이를 갖도록하며 0으로 초기화)
    answer = [0 for _ in range(len(id_list))]       # 담아야 하는 값 : id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수

    # 신고한 유저와 신고당한 유저를 저장할 딕셔너리 (key : 신고한 유저, value : 해당 유저에게 신고 당한 유저들)
    reporting_dict = dict()

    # 신고당한 유저들 이름만 따로 모아놓을 리스트 (몇번 신고 당했는지 세기 위해서)
    # (ex.["frodo","frodo","neo","neo","muzi"])
    reported_ppl = []

    # 딕셔너리 초기 셋팅 (key에 각 유저 id를 넣고, value에는 빈 리스트 넣어주기)
    for id in id_list:
        reporting_dict[id] = []

    # 딕셔너리 채우기 작업
    for r in report:
        key = (r.split(' '))[0]     # 신고한 유저
        value = (r.split(' '))[-1]  # 해당 유저에게 신고당한 유저

        reported_ppl.append(value)
        reporting_dict[key].append(value)

    # print(reporting_dict)
    # print(reporting_dict.values())
    # print(reported_ppl)
    # print(reporting_dict.items())

    # 신고당한 유저들이 id_list 인덱스 순서 기준대로 몇번 신고당했는지 기록할 리스트
    # (ex. [1, 2, 0, 2] - 순서대로 ["muzi", "frodo", "apeach", "neo"] 가 신고당한 횟수)
    reported_count = [0 for _ in range(len(id_list))]

    # 신고당한 유저들 리스트를 토대로 id_list에 있는 id 순서대로 신고당한 횟수 ban_ppl 리스트에 기록하기
    for reported_person in reported_ppl:
        if(reported_person in id_list):
            index = id_list.index(reported_person)
            reported_count[index] += 1

    # 신고당한 횟수를 기록한 리스트 reported_count를 통해 딕셔너리를 참조하여 누가 신고하였는지 찾기
    # 만약 k번 이상 신고당하였다면 -> 정지 -> 신고한 사람이 처리메일을 받게됨 -> answer에 기록되어야함
    for key, value in reporting_dict.items():
        for i in range(len(reported_count)):

            if(reported_count[i] >= k):     # k번 이상 신고당하면
                ban_id = id_list[i]         # 이 id는 정지를 먹게됨

                if(ban_id in value):        # 만약 정지를 먹는 id를 신고한 적이 있다면, 처리메일을 받게 되므로 answer에 기록되어야 함
                    index = id_list.index(key)      # 인덱스는 신고한 사람인 key 값의 id_list 위치
                    answer[index] += 1              # 그 사람이 메일받았으니 기록

    # print(ban_ppl)

    return answer


if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
                   2))

    print(solution(["con", "ryan"],
                   ["ryan con", "ryan con", "ryan con", "ryan con"],
                   3))
