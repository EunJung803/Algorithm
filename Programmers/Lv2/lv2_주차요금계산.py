import math

def solution(fees, records):
    answer = []

    # 입차 -> 출차 X : 23:59 출차로 계산
    # 누적 주차 시간 <= 기본 시간 : 기본 요금
    # 누적 주차 시간 > 기존 시간 : 기본 요금 + 초과 시간 (나누어 떨어지지 않으면 올림 계산)
    # fee : [기본 시간, 기본 요금, 단위 시간, 단위 요금]

    ## TODO
    ### IN 이면 -> 차량 번호 사전에 기록
    ### OUT 이면 -> 사전에서 차량번호 찾아서 시간 계산
    ### 시간 계산은 -> (시간 + 분 / 60) * 60 의 반올림
    ### 계산하고 나서 사전에서 제거 -> 마지막에 사전에 남아있는 차들은 아직 출차 못한 차 -> 23:59로 계산

    car_record = dict()     # 입차한 차의 시간을 기록해놔서 출차하는 같은 차번호를 발견할 때 꺼내서 계산하기 위한 사전
    ans_record = dict()     # 해당 차 번호에 대한 누적 주차 시간을 계산해서 저장할 사전

    for r in records:
        rec = list(r.split(" "))

        # 입차하는 차라면
        if(rec[2] == "IN"):
            car_record[rec[1]] = rec[0]         # car_record 에 기록
            if(int(rec[1]) not in ans_record):  # ans_record 에 없는 차라면 시간 0으로 새로 넣어주기 (추후 key값의 정렬을 위해 차 번호는 int형으로 넣어줌)
                ans_record[int(rec[1])] = 0

        # 출차하는 차라면
        elif(rec[2] == "OUT"):
            in_time = car_record.get(rec[1])    # 출차하는 차 번호를 가지고 입차한 시간 기록을 얻기
            out_time = rec[0]       # 출차 시간

            # 시간 계산
            calculated_time = round(((int(out_time.split(":")[0]) + (int(out_time.split(":")[1]) / 60)) - (int(in_time.split(":")[0]) + (int(in_time.split(":")[1]) / 60))) * 60)
            # print(calculated_time)

            ans_record[int(rec[1])] += calculated_time      # 누적 주차 시간 기록하기
            car_record.pop(rec[1])      # 출차했으니까 입차 기록에서 제거

    # 입차한 차가 남아있으면 -> 입차 이후 출차한 내역이 없는 차
    if(len(car_record) > 0):
        for c in car_record:
            # 23:59에 출차된 것으로 간주해서 계산하기
            calculated_time = round(abs(((23 + (59 / 60)) - (int(car_record[c].split(":")[0]) + (int(car_record[c].split(":")[1]) / 60))) * 60))
            ans_record[int(c)] += calculated_time       # 누적 주차 시간에 기록하기

    # 차량 번호가 작은거부터 정답을 출력해야하니 정렬하기
    ans_record = sorted(ans_record.items())

    # 요금 계산해서 정답 배열에 넣기
    for i in ans_record:
        if (i[1] <= fees[0]):       # 기본 시간 이하라면 -> 기본 요금 청구
            cal_fee = fees[1]
        else:                       # 기본 시간을 초과하면 -> 기본 요금 + 단위 시간마다 단위 요금을 청구
            cal_fee = fees[1] + (math.ceil((i[1] - fees[0]) / fees[2]) * fees[3])
        answer.append(cal_fee)


    return answer

if __name__ == '__main__':
    print(solution([180, 5000, 10, 600],
                   ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

