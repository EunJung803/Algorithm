from collections import Counter

def solution(input_string):
    answer = ''

    # 2회 이상 나타난 알파벳이 2개 이상의 부분으로 나뉘어 있으면 == 외톨이 알파벳
    # 외톨이 알파벳 예시
    # "e(d)eaaabbcc(d)"
    # "(ee)dd(ee)"

    input_alpha = sorted(list(Counter(input_string).keys()))    # input_string에 있는 알파벳 종류들을 담은 list 생성
    # (정답을 알파벳 순으로 내줘야하기 때문에 미리 정렬하기)
    # print(input_alpha)

    for i in range(len(input_alpha)):
        index_check = []
        for j in range(len(input_string)):
            if (input_string[j] == input_alpha[i]):     # 알파벳 종류가 확인되면 해당 알파벳의 인덱스 번호를 다 담아두기
                index_check.append(j)

        for c in range(len(index_check)):       # 담아둔 인덱스 번호를 돌 때, 하나라도 인덱스 번호가 연속된게 없다면 -> 외톨이 알파벳
            if (c + 1 == len(index_check)):
                break
            if (index_check[c] + 1 != index_check[c + 1]):
                answer += input_alpha[i]
                break

    if (len(answer) == 0):      # 아무것도 안담겼으면 외톨이 알파벳이 없음 N
        answer = "N"

    return answer