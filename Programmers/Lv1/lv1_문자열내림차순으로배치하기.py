def solution(s):
    answer = ''

    list_s = list(s)
    list_s.sort(reverse=True)

    for i in list_s:
        answer += i

    return answer


print(solution("Zbcdefg"))