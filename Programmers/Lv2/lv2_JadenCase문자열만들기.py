def solution(s):
    answer = ''

    s_split = list(s.split(" "))
    for i in range(len(s_split)):
        if(s_split[i] == ""):
            answer += " "
        else:
            if not(s_split[i][0].isdigit()):
                answer += s_split[i][0].upper() + s_split[i][1:].lower()
            else:
                answer += s_split[i][0] + s_split[i][1:].lower()

            if(i != len(s_split)-1):
                answer += " "

    # print(s_split)

    if(s_split[-1] == ""):
        answer = answer[0:len(s)]

    return answer


if __name__ == '__main__':
    # print(solution("3people unFollowed me"))
    print(solution("for  the  last week   "))
