def solution(t, p):
    answer = 0

    start = 0
    for i in range(len(p), len(t) + 1):
        sub_str = t[start: i]
        # print(sub_str)
        if (int(p) >= int(sub_str)):
            answer += 1
        start += 1

    return answer