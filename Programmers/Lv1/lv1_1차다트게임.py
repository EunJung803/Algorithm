import math

def solution(dartResult):
    answer = 0

    dart_split = []         # input으로 들어온 문자열 dartResult를 쪼개서 담을 리스트
    score = []              # 아래 for문에서 각 점수를 쪼깨어 부분 리스트로 넣을 리스트

    # 문자열 쪼개서 담기 작업
    for d in dartResult:
        if(d.isdigit()):            # 만약 숫자면
            score.append(int(d))    # int로 변형해서 부분 리스트 score에 넣어두기
        else:                       # 숫자가 아니면 (ex. 'S', 'D', 'T', '*', '#')
            score.append(d)         # 그냥 string 형식 그대로 부분 리스트 score에 넣어두기

        # 부분 리스트인 score 의 길이가 3 이상이라면 -> 점수가 10이라는 소리
        # (10은 2자리라서 score에 이렇게 1과 0으로 쪼개어져 들어가있게됨 ex. [1, 0, 'S'])
        if (len(score) >= 3):
            update = str(score[0]) + str(score[1])      # 맨앞에 두 정수를 붙여서 새로운 정수로 만들어주기 (ex. '1' + '0' -> '10)
            score[0] = int(update)      # 0번째 자리에 새로 만든 2자리 정수를 넣고 (ex. [10, 0 'S'])
            score.pop(1)                # 1번 인덱스에 있는건 빼버리기 (ex. [10, 'S'])

        # 만약 옵션인 *이나 #이 있다면 -> 따로 분리해서 넣어주기
        if (d == '*' or d == '#'):
            dart_split.append(score)    # 부분 리스트 score를 dart_split 리스트에 넣기
            score = []                  # 초기화

        # 보너스를 만나면 -> 끊어주기
        if(d == 'S' or d == 'D' or d == 'T'):       # 부분 리스트 score를 dart_split 리스트에 넣기
            dart_split.append(score)                # 초기화
            score = []

    print(dart_split)
    # dart_split 출력 예시 (ex. [[1, 'S'], [2, 'D'], ['*'], [3, 'T']])

    calculate_score = []        # 각 점수를 계산할 리스트

    for element_index, element in enumerate(dart_split):        # 위의 예시를 토대로 하면 element : [1, 'S'], element_index : 0

        # S, D, T를 기반으로 제곱 계산하기
        if(element[-1] == 'S'):
            calculate_score.append(math.pow(element[0], 1))
        if (element[-1] == 'D'):
            calculate_score.append(math.pow(element[0], 2))
        if (element[-1] == 'T'):
            calculate_score.append(math.pow(element[0], 3))

        # 만약 옵션 *이 있으면
        if(element[-1] == '*'):
            index = dart_split.index(element, element_index)    # 옵션 *의 인덱스 파악

            # 옵션 *이 첫번째 점수에서 나온게 아닐 때
            if(index >= 2):
                current_index = len(calculate_score) - 1        # 가장 최근 calculate_score에 계산되어 들어온 값의 인덱스
                calculate_score[current_index] *= 2             # *을 가진 해당 점수 2배하기
                calculate_score[current_index - 1] *= 2         # 해당 점수 바로 전에 얻은 점수 2배하기

            # 옵션 *이 첫번째 점수에서 나온거일 때
            else:
                calculate_score[index - 1] *= 2     # 현재 첫번째 점수만 2배

        # 만약 옵션 #이 있으면
        if (element[-1] == '#'):
            current_index = len(calculate_score) - 1        # 가장 최근 calculate_score에 계산되어 들어온 값의 인덱스
            calculate_score[current_index] *= (-1)          # #을 가진 해당 점수 마이너스화

    print(calculate_score)
    # calculate_score 출력 예시 (ex. [2.0, 8.0, 27.0])

    # 총 합 계산하기
    for score in calculate_score:
        answer += score

    return answer


if __name__ == '__main__':
    print(solution("1S2D*3T"))
    print(solution("1D2S#10S"))
    print(solution("1D2S0T"))
    print(solution("1S*2T*3S"))
    print(solution("1D#2S*3S"))
    print(solution("1T2D3D#"))
    print(solution("1D2S3T*"))
    print(solution("1S2D*3T*"))     # 72
    print(solution("1S*2D*3T*"))    # 74
    print(solution("10S1S0S*"))     # 12
    print(solution("1T*2T#3T*"))
