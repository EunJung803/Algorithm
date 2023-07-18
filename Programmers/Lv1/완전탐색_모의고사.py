def count_supoja(supoja, answers):
    count = 0
    j = 0

    # 수포자가 몇개나 맞추는지 세는 과정
    for i in range(len(answers)):   # answers의 길이만큼 비교하는데
        if(j >= len(supoja)):       # 만약 수포자의 패턴을 담고있는 배열의 길이보다 큰 인덱스가 온다면 -> 수포자의 배열 안에서 루틴으로 돌게 해야함
            j = j % len(supoja)     # 나머지를 통해 수포자 배열 속 몇번째 인덱스인지 찾기 (ex. [1,2,3,4,5] 에서 7번째 인덱스라면, 7 % 5 = 2 -> 즉 2번째 인덱스를 가르킴)
        if(answers[i] == supoja[j]):        # 아직 크지 않다면, 같은지 비교 -> 같으면 count 올리기
                count += 1
        j += 1

    return count


def solution(answers):
    answer = []

    # 수포자 1: 12345 반복
    # 수포자 2: 21 23 24 25 반복
    # 수포자 3: 33 11 22 44 55 반복
    supoja1 = [1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    supo_1 = count_supoja(supoja1, answers)     # 수포자 1의 점수
    supo_2 = count_supoja(supoja2, answers)     # 수포자 2의 점수
    supo_3 = count_supoja(supoja3, answers)     # 수포자 3의 점수

    # print(supo_1)
    # print(supo_2)
    # print(supo_3)

    supo_count = [supo_1, supo_2, supo_3]   # 수포자들의 점수를 담은 배열

    # 점수로 누가 제일 높은 점수를 받았는지 정답 찾아내기
    for i in range(len(supo_count)):
        if(max(supo_count) == supo_count[i]):       # 인덱스 i의 값이 배열의 최대 값이라면, 높은 점수를 받은 수포자 -> 정답에 추가
            answer.append(i+1)

    return answer

if __name__ == '__main__':
    print(solution([1,2,3,4,5]))
    print(solution([1,3,2,4,2]))
    print(solution([5, 5, 5, 5, 5, 5, 5, 5]))           # [1, 2]
    print(solution([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))     # [1, 3]
    print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))     # [1, 2, 3]