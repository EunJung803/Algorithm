def solution(today, terms, privacies):
    answer = []

    # terms -> 약관종류 유효기간
    # privacies -> 날짜 약관종류
    # privacies에 있는 날짜에 약관 유효기간을 더했을 때, 현재 날짜와 비교

    today_year = int(today.split(".")[0])       # 현재 년도
    today_month = int(today.split(".")[1])      # 현재 월
    today_day = int(today.split(".")[2])        # 현재 날짜

    terms_dict = dict()     # 약관에 대한 유효기간을 저장할 딕셔너리 (key : 약관종류, value : 유효기간)
    for i in terms:     # 딕셔너리 채우기
        terms_dict[i.split(" ")[0]] = i.split(" ")[1]

    for i in range(len(privacies)):
        p_date = privacies[i].split(" ")[0]  # 개인정보수집일자
        p_term = privacies[i].split(" ")[1]  # 약관 종류

        # 개인정보수집일자의 년도, 월, 날짜 분류
        year = int(p_date.split(".")[0])
        month = int(p_date.split(".")[1])
        day = int(p_date.split(".")[2])

        month += int(terms_dict.get(p_term))    # 선택된 약관의 유효기간을 사전에서 가져와서 현재 월 수에 더해줌

        if(month > 12):     # 만약 12가 넘는 월 수가 된다면, 년도가 바뀌어야 함
            if(month % 12 == 0):        # 12의 배수인 월 수일 때 -> 12월인건 고정
                year += month // 12 - 1
                month = 12
            else:                       # 12의 배수가 아닌 월 수일 때
                year += month // 12
                month = month % 12

        # 유효기간을 넘었는지 파악
        if(today_year > year):      # 년도가 넘었다면 무조건 지남
            answer.append(i + 1)
        if(today_year == year):         # 년도는 같은데
            if(today_month > month):    # 월 수가 넘었다면 무조건 지남
                answer.append(i + 1)
            elif(today_month == month):     # 만약 월 수도 같다면
                if(today_day >= day):       # 날짜로 비교 -> 날짜가 크다면 지남
                    answer.append(i + 1)

    return answer


if __name__ == '__main__':
    print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
    print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
    print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.05.02 A", "2021.05.02 A", "2022.02.20 C"]))     # privacies에 같은 날짜 여러개
    print(solution("2021.12.08", ["A 18"], ["2020.06.08 A"]))       # month가 12의 배수