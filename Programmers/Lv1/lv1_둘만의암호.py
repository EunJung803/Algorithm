def solution(s, skip, index):
    answer = ''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in skip:
        alphabet = alphabet.replace(i, "")      # skip에 포함되어 있는 글자는 지워버리기
    for i in s:
        char = alphabet.index(i) + index        # index만큼 뒤의 알파벳 구하기
        if(char >= len(alphabet)):              # 만약 z를 넘어간다면
            char = char % len(alphabet)         # a부터 다시 시작
        answer += alphabet[char]

    return answer


if __name__ == '__main__':
    print(solution("aukks", "wbqd", 5))
    print(solution("aaaaz", "bcde", 5))  # jjjji
