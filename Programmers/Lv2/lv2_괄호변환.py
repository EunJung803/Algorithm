# "올바른 괄호 문자열"인지 판별하는 함수 (맞다면 True)
def check_perfect(string):
    left_bracket = []
    check = True
    for i in range(len(string)):
        if (string[i] == '('):
            left_bracket.append(string[i])
        elif (string[i] == ')'):
            if (left_bracket):
                left_bracket.pop()
            else:
                check = False
    return check

# u와 v로 분리하는 함수 (u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.)
def split_u_v(string):
    left_cnt, right_cnt = 0, 0
    u, v = '', ''
    if (len(string) == 0):
        return u, v

    for i in range(len(string)):
        if (string[i] == '('):
            left_cnt += 1
        elif (string[i] == ')'):
            right_cnt += 1
        if (left_cnt == right_cnt):
            u = string[:i + 1]
            v = string[i + 1:]
            break

    return u, v

# 괄호 방향을 뒤집어주는 함수
def reverse_bracket(string):
    reverse_str = ''
    for i in range(len(string)):
        if (string[i] == '('):
            reverse_str += ')'
        if (string[i] == ')'):
            reverse_str += '('
    return reverse_str

def solution(p):
    # p가 "올바른 괄호 문자열"인지 확인
    if (check_perfect(p)):
        return p

    u, v = split_u_v(p)     # u, v로 쪼개기 (2번)

    if(check_perfect(u)):   # u가 "올바른 괄호 문자열"인 경우 (3번) -> u는 그대로 두고 v에 대해서 재귀적으로 수행
        return u + solution(v)
    else:                   # u가 "올바른 괄호 문자열"이 아닌 경우 (4번) -> 4-1번 ~ 4-5번 수행
        answer = '(' + solution(v) + ')' + reverse_bracket(u[1:-1])

    return answer

"""
### 이전코드
def solution(p):
    answer = ''

    # ( 개수 == ) 개수 : 균형잡힌 괄호 문자열
    # () 짝도 다 맞으면 : 올바른 괄호 문자열
    # 균형잡힌 괄호 문자열을 -> 올바른 괄호 문자열로 변환하기

    ## 변환방법
    # u, v 로 쪼개기 -> u는 균형잡힌 괄호 문자열 (최소), v는 비어있을 수 있음
    # u가 올바른 괄호 문자열이면 -> v는 1부터 다시 수행 -> u에 붙여서 반환
    # u가 올바른 괄호 문자열이 아니면 -> 빈 문자열에 ( 붙이기 -> v부터 1단계 수행, 이어붙이기 -> ) 붙이기 -> u의 앞 뒤 제거 -> 나머지 방향 뒤집어서 뒤에 붙이기

    u, v = '', ''
    new_u, new_v = '', ''
    sub = ''

    # p가 올바른 괄호 문자열인지 확인
    check = check_perfect(p)

    if (check):
        return p

    # p가 올바른 괄호 문자열이 아니라면
    list_u = []
    list_v = []
    if (check == False):
        u, v = split_u_v(p)
        list_u.append(u)
        list_v.append(v)
        new_u = u
        while (check_perfect(new_u) == True):
            new_u, new_v = split_u_v(v)
            list_u.append(new_u)
            list_v.append(new_v)
            v = new_v

        sub_list_u = []
        for i in range(len(list_v) - 1, -1, -1):
            if (check_perfect(list_u[i]) == False):
                sub += '(' + list_v[i] + ')' + reverse_bracket(list_u[i][1:-1])
            elif (check_perfect(list_u[i]) == True):
                sub_list_u.append(list_u[i])
            for j in range(len(sub_list_u)):
                sub = sub_list_u[j] + sub
                sub_list_u.pop()
        answer = sub

    return answer
"""

if __name__ == '__main__':
    print(solution("()))((()"))     #  "()(())()"