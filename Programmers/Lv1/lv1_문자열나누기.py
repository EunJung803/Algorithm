def solution(s):
    answer = 0

    # 첫글자 = x
    # x와 같은 글자 수 == x가 아닌 글자 수 -> 분리
    # 기존 문자열에서 분리된 부분 제거 -> 반복

    same_s, diff_s = 0, 0   # 같은 글자 수, 다른 글자 수
    ans = []                # 분리되는 문자열을 담을 배열

    x_index = 0         # x의 인덱스를 담을 변수
    x = s[x_index]      # 초기 x값은 맨 첫번째 문자로 설정

    for i in range(0, len(s)):
        # 같은 글자 수, 다른 글자 수 세기
        if (x == s[i]):
            same_s += 1
        if (x != s[i]):
            diff_s += 1

        # 두 글자 수가 같으면 -> 분리
        if (same_s == diff_s):
            ans.append(s[x_index : i + 1])      # x부터 i까지 분리하고
            x_index = i + 1         # x는 분리된 이후의 문자열에서의 첫번째 글자

            if (x_index + 1 >= len(s)):     # 만약 거의 다 분리되어서 이제 남아있는 인덱스를 넘어가면
                ans.append(s[x_index:])     # 지금까지 읽은 문자열을 분리하고 종료
                break

            x = s[x_index]              # x 재설정
            same_s, diff_s = 0, 0       # 초기화

        # 두 글자 수가 다르지만, 더 이상 읽을 글자가 없으면
        if(same_s != diff_s and i+1 >= len(s)):
            ans.append(s[x_index:])     # 지금까지 읽은 문자열을 분리하고 종료
            break

    # print(ans)
    ans = list(filter(None, ans))       # 리스트 내 '' 같은 공백 제거
    answer = len(ans)                   # 분리된 문자열이 담긴 배열의 길이가 정답
    return answer

if __name__ == '__main__':
    print(solution("banana"))
    print(solution("abracadabra"))
    print(solution("aaabbaccccabba"))
    print(solution("aaabbbc"))
    print(solution("aabcddnaaaaccbb"))
    print(solution("a"))