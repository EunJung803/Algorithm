def solution(book_time):
    answer = 0

    ans = []
    book_time = sorted(book_time)       # 대실 시작 시간이 이른것부터 정렬

    for i in range(len(book_time)):
        room = []
        # 비어있는 시간이라면 -> 이미 다른 방으로 예약됨 (넘어가기)
        if (len(book_time[i]) == 0):
            continue

        room.append(book_time[i])       # book_time[i] 삽입
        end_time = book_time[i][1].split(":")                               # book_time[i]의 퇴실 시간 구하기
        end_time_min = (int(end_time[0]) * 60) + int(end_time[1]) + 10      # 퇴실 시간을 분 기준으로 변환하고 청소시간 10분을 더해두기

        for j in range(i + 1, len(book_time)):          # 다음 시간대의 방이 바로 이 방에 예약될 수 있는지 따져보기
            # 비어있는 시간이라면 -> 이미 다른 방으로 예약됨 (넘어가기)
            if(len(book_time[j]) == 0):
                continue

            next_start_time = book_time[j][0].split(":")        # book_time[j]의 입실 시간 구하기
            next_start_time_min = (int(next_start_time[0]) * 60) + int(next_start_time[1])      # 입실 시간을 분 기준으로 변환

            if (end_time_min <= next_start_time_min):   # i번째 시간의 퇴실 시간 + 청소시간 이어도 입실 가능한 시간이라면
                room.append(book_time[j])       # 바로 그 방의 다음 손님으로 입실

                # 그 다음 방이 연속으로 입실할 수 있는지 따지기 위해 새로운 퇴실시간을 j번째 요소로 갱신
                new_end_time = book_time[j][1].split(":")
                end_time_min = (int(new_end_time[0]) * 60) + int(new_end_time[1]) + 10
                book_time[j] = []       # 이미 방이 지정되었으므로 비우기

        ans.append(room)

    print(ans)
    answer = len(ans)

    return answer

if __name__ == '__main__':
    print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
    print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["12:30", "13:20"]]))
