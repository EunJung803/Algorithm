def solution(s):
    answer = ''

    s_split = list(s.split(" "))    # 공백으로 split하여 문자 담아놓기

    for i in range(len(s_split)):
        # 만약 연속된 공백이라면 split 했을 때 "" 가 리스트 안에 존재
        if(s_split[i] == ""):
            answer += " "

        # 연속된 공백이 아니라면 (문자인 경우)
        else:
            # 맨 앞글자가 숫자가 아닐 때
            if not(s_split[i][0].isdigit()):
                answer += s_split[i][0].upper() + s_split[i][1:].lower()
            # 맨 앞글자가 숫자일 때
            else:
                answer += s_split[i][0] + s_split[i][1:].lower()

            if(i != len(s_split)-1):    # 맨 끝 문자가 아니라면 문자 간의 공백이 중간에 있으니 공백 추가
                answer += " "

    # 연속된 공백이 맨 끝에 붙는다면 마지막 문자 뒤에 공백이 추가로 붙어서 공백 수가 안맞음 -> 고로 공백 하나 제거를 위해 맨 끝 제거
    if(s_split[-1] == ""):
        answer = answer[0:len(s)]

    return answer


if __name__ == '__main__':
    # print(solution("3people unFollowed me"))
    print(solution("for  the  last week   "))
