def solution(strings, n):
    answer = []

    strings.sort()

    std_list = []

    for i in range(len(strings)):
        std_list.append(strings[i][n])

    std_list.sort()

    for i in std_list:
        for j in range(len(strings)):
            if(i == strings[j][n]):
                if(strings[j] not in answer):
                    answer.append(strings[j])

    return answer

if __name__ == '__main__':
    print(solution(["sun", "bed", "car"], 1))
    print(solution(["abce", "abcd", "cdx"], 2))