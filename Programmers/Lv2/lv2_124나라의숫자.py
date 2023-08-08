def solution(n):
    answer = ''

    list_124 = [1, 2, 4]

    while(n > 0):       # 3진법 이용하기
        answer += str(list_124[(n % 3) - 1])
        n = (n - 1) // 3

    answer = "".join(reversed(answer))      # 오른쪽에서 밀어넣어서 만든 답이니 거꾸로 한번 뒤집어줘야함

    return answer

if __name__ == '__main__':
    # print(solution(3))
    # print(solution(8))
    print(solution(9))
    # print(solution(10))
    # print(solution(12))
    # print(solution(13))