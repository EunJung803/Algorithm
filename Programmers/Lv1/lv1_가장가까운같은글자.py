def solution(s):
    answer = []

    word = ''
    for i in range(len(s)):
        if (s[i] in word):
            answer.append(i - word.rindex(s[i]))
        else:
            answer.append(-1)

        word += s[i]

    return answer

if __name__ == '__main__':
    print(solution("banana"))
    print(solution("foobar"))