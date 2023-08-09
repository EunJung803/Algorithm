def solution(s):
    answer = ''

    s = list(s.split(" "))
    s = list(map(int, s))
    answer += str(min(s)) + " " + str(max(s))

    return answer
