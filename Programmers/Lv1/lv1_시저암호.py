def solution(s, n):
    answer = ''

    for i in s:

        # 소문자인 경우
        if(i.islower()):
            current_ord = ord(i) + n        # 현재 문자에 n만큼 이동한 아스키코드 값
            if(current_ord > ord('z')):     # 만약 최대 알파벳인 z를 넘어가는 값이라면, 다시 a부터 순환하도록 해야하므로 값을 바꿔줘야 한다.
                answer += chr(ord('a') + (current_ord - ord('z') - 1))      # z를 넘어서 이동한 만큼의 값을 다시 a부터 이동하면 된다.
            else:
                answer += chr(current_ord)

        # 대문자인 경우
        if (i.isupper()):
            current_ord = ord(i) + n
            if (current_ord > ord('Z')):
                answer += chr(ord('A') + (current_ord - ord('Z') - 1))
            else:
                answer += chr(current_ord)

        # 공백인 경우
        if(i == ' '):
            answer += ' '

    return answer


### 소문자
# s = 'a'
# print(ord(s))
# s = 'z'
# print(ord(s))
# 97 ~ 122

### 대문자
# s = 'A'
# print(ord(s))
# s = 'Z'
# print(ord(s))
# 65 ~ 90


if __name__ == '__main__':
    print(solution("AB", 1))        # BC
    print(solution("z", 1))         # a
    print(solution("a B z", 4))     # e F d
    print(solution("bCa", 25))      # aBz