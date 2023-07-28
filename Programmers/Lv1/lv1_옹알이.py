def solution(babbling):
    answer = 0

    speak = ["aya", "ye", "woo", "ma"]
    # speak에서 조합해서 완성되는 단어만 발음 가능
    # 같은거 두번을 조합해서는 발음 불가능

    # 네가지 발음과 정확히 똑같은 발음이 있는 경우 확인하기 -> 존재한다면 발음할 수 있으니 answer에 +1 해주고 다음 검사는 건너뛰도록 제거
    for bab in babbling:
        if(bab in speak):
            answer += 1
            babbling.remove(bab)

    # 발음할 수 있는지 검사하기
    for bab in babbling:
        can_speak = True        # 발음할 수 있는지 아닌지 확인하기 위한 변수
        while (len(bab) > 0):
            if ("aya" in bab):
                bab = bab.replace("aya", "1")
            if ("ye" in bab):
                bab = bab.replace("ye", "2")
            if ("woo" in bab):
                bab = bab.replace("woo", "3")
            if ("ma" in bab):
                bab = bab.replace("ma", "4")
            else:
                break

        if(bab.isdigit()):      # 완벽하게 숫자로 모두 다 replace 되었다면 -> 4가지를 붙여 만들 수 있는 발음들
            for i in range(len(bab)-1):     # 같은 발음을 연속으로 하는지 확인
                if(bab[i] == bab[i+1]):     # 연속으로 하는 발음이라면 -> 발음할 수 없음
                    can_speak = False       # False로 변경
                    break
        else:                   # 모두 완벽하게 숫자로 replace되지 않은 경우 (중간에 치환되지 못한 글자가 존재, 즉 발음할 수 없는 단어)
            can_speak = False   # False로 변경

        if(can_speak):      # 만약 can_speak가 True라면 -> 발음 가능
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(["aya", "yee", "u", "maa"]))
    print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
    # 아래는 반례 케이스들
    print(solution(["yayae"]))                  # 0
    print(solution(["ayayeaya"]))               # 1
    print(solution(["ayayeye"]))                # 0
    print(solution(["ayayeayayeayaaya"]))       # 0
    print(solution(["ayayemaaya"]))             # 1
    print(solution(["yeye", "yeye"]))           # 0