def solution(s):
    ans = ''
    str_num = ''

    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for num in s:
        if (num.isdigit()):     # 숫자면 그냥 추가
            ans += num
        else:       # 숫자가 아니면 -> 영단어 -> 무슨 숫자의 영단어인지 찾기
            str_num += num
            # 사전 안에 없는 영단어라면 아직 글자가 덜 들어온 것 (get 했을 때 None이 나오게됨)
            if (num_dict.get(str_num) != None):         # None이 아니라면 영단어를 찾을 수 있게됨
                ans += num_dict.get(str_num)            # 영단어로 찾은 숫자 추가
                str_num = ''                    # 다음 영단어 완성을 위해 초기화

    return int(ans)     # 모인 숫자를 str로 붙여줬으니 최종적으로는 int 형식으로 리턴

if __name__ == '__main__':
    print(solution("one4seveneight"	))
    print(solution("23four5six7"))
    print(solution("2three45sixseven"))
    print(solution("123"))