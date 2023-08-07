def solution(record):
    answer = []

    # Enter / Leave / Change
    # uid
    # 닉네임

    result = []
    nickname_dict = dict()

    for rec in record:
        record_list = list(rec.split(" "))
        if (record_list[0] == "Enter"):
            nickname_dict[record_list[1]] = record_list[2]
            ans_str = record_list[1] + "님이 들어왔습니다."
            result.append(ans_str)
        if (record_list[0] == "Change"):
            nickname_dict[record_list[1]] = record_list[2]
        if (record_list[0] == "Leave"):
            ans_str = record_list[1] + "님이 나갔습니다."
            result.append(ans_str)

    for i in result:
        uid = list(i.split("님"))[0]
        ans = i.replace(uid, nickname_dict.get(uid))
        answer.append(ans)

    return answer

if __name__ == '__main__':
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
