# def solution(a, b):
#     answer = ''
#
#     # 윤년 -> 2월이 29일까지 있음
#
#     # month_31 = [1, 3, 5, 7, 8, 10, 12]
#     # month_30 = [4, 6, 9, 11]
#     # month_29 = [2]
#
#     starting_days = ['FRI', 'MON', 'TUE', 'FRI', 'SUN', 'WED', 'FRI', 'MON', 'THU', 'SAT', 'TUE', 'THU']    # 각 월별 시작 요일들
#     days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']    # 요일 리스트
#
#     starting_days_in_a = starting_days[a - 1]       # a월의 시작하는 요일 찾기
#     # print(starting_days_in_a)
#     start_index = days.index(starting_days_in_a)    # a월의 시작하는 요일이 days에서는 몇번째 인덱스인지 찾기
#     # print(start_index)
#     if((start_index + (b % 7 - 1)) >= 7):                   # b일의 요일 리스트 속 인덱스를 찾는데 만약 7보다 크다면 (인덱스 범위를 벗어난다면)
#         answer = days[(start_index + (b % 7 - 1)) - 7]      # 7을 빼준다
#     else:
#         answer = days[start_index + (b % 7 - 1)]
#
#     return answer

def solution(a, b):
    answer = ''

    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']     # 1/1이 FRI부터 시작했으니 인덱스 1이 FRI인 요일 순서의 리스트
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    # 각 월이 가지고 있는 총 일 수를 담은 리스트

    total_days = sum(month[:a - 1], b)      # a월 b일 의 총 일 수
    answer += day[total_days % 7]           # a월 b일 이 가지고 있는 총 일 수를 구한 뒤, 총 일 수를 통해 요일을 찾을 수 있다.
                                            # 일주일 7일을 기반으로 반복되는 요일 리스트 day의 인덱스를 기반으로 7로 나눴을 때의 나머지를 통해 a월 b일의 요일을 찾는다.

    return answer

if __name__ == '__main__':
    print(solution(5, 24))
    print(solution(4, 4))       # MON
    print(solution(4, 1))       # FRI
    print(solution(6, 13))      # MON