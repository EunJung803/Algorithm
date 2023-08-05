def check_gualho(s):
    arr = []
    for i in s:
        # 여는 괄호일 때
        if(i == "[" or i == "{" or i == "("):
            arr.append(i)
        # 닫는 괄호일 때
        else:
            if(len(arr) == 0):  # 여는 괄호가 없는데 닫는 괄호가 들어오면 -> 올바른 괄호가 절대 아님
                arr = [-1]
                return arr
            # 각자 알맞게 여는 괄호가 짝지어지면 -> arr에서 pop
            if(i == "]"):
                if (arr[-1] == "["):
                    arr.pop(-1)
                else:
                    arr.append(i)
            if(i == "}"):
                if (arr[-1] == "{"):
                    arr.pop(-1)
                else:
                    arr.append(i)
            if(i == ")"):
                if (arr[-1] == "("):
                    arr.pop(-1)
                else:
                    arr.append(i)
    return arr


def solution(s):
    answer = 0

    # s를 왼쪽으로 x칸 만큼 회전 == 맨 왼쪽 괄호부터 떼어내서 오른쪽에 하나씩 붙여감
    # 올바르지 않은 괄호 : 열려있는데 닫히지 않음, 닫혀있는게 먼저 나옴

    for x in range(len(s)):
        ans_arr = check_gualho(s)   # 올바른 괄호인지 체크
        if(len(ans_arr) == 0):      # 올바른 괄호라면 리턴값의 배열 길이가 0
            answer += 1
        s = s[1:] + s[0]    # 회전

    return answer


if __name__ == '__main__':
    print(solution("[](){}"))
    print(solution("}]()[{"))
    print(solution("}}}"))
    print(solution("{(})"))
    print(solution("[({})]"))
