def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # print(answer)

    # 2단계
    for i in answer:
        if (i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.'):
            continue
        else:
            answer = answer.replace(i, "")
    # print(answer)

    # 3단계
    while(".." in answer):
        answer = answer.replace("..", ".")

    # 4단계
    if(len(answer) > 0):
        if(answer[0] == "."):
            answer = answer[1:]
    if (len(answer) > 0):
        if (answer[-1] == "."):
            answer = answer[:-1]
    # print(answer)

    # 5단계
    if(len(answer) == 0):
        answer = "a"

    # 6단계
    if(len(answer) >= 16):
        answer = answer[:15]
        if(answer[-1] == "."):
            answer = answer[:14]
    # print(answer)

    # 7단계
    if(len(answer) <= 2):
        repeat = answer[-1]
        while(len(answer) < 3):
            answer += repeat
    # print(answer)

    return answer

if __name__ == '__main__':
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))
    print(solution("1234567890.123.456"))   # 1234567890.123
    print(solution("a..a"))     # a.a
    print(solution("....s"))    # sss
    print(solution(".1234..........5678."))
    print(solution(""))