def solution(s):
    answer = 0

    ### 실패 코드 (효율성 똥망)
    # for i in range(len(s)):
    #     if(len(s) == 0):
    #         break
    #     if (i >= len(s)-1):
    #         if (len(s) == 2 and s[0] == s[1]):
    #             s = s.replace(s[0] * 2, "")
    #         else:
    #             break
    #     elif (s[i] == s[i + 1]):
    #         s = s.replace(s[i] * 2, "")

    stack = []
    for i in range(len(s)):
        stack.append(s[i])      # stack에 하나씩 넣어주면서
        if(len(stack) >= 2 and stack[-2] == stack[-1]):     # stack에 들어있는 요소들 중 가장 마지막 2개가 같은지 비교
            stack.pop(-1)       # 같다면 짝지어서 제거
            stack.pop(-1)

    if (len(stack) == 0):       # stack이 다 짝지어져서 비어있다면 1
        answer = 1
    if (len(stack) != 0):       # 짝지어지지 않아서 요소가 남아있다면 0
        answer = 0

    return answer

if __name__ == '__main__':
    print(solution("baabaa"))
    print(solution("cdcd"))
    print(solution("abbcdaadca"))   # 1

