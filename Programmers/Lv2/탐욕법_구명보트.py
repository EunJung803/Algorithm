def solution(people, limit):
    answer = 0

    people = sorted(people)     # 정렬해서 (가벼운 사람 + 무거운 사람) 조합으로 최적의 해를 구해야함

    start = 0
    end = len(people) - 1

    while (start <= end):
        # 무게 제한보다 크다면 -> 마지막 인덱스를 가르키는 end 한칸 앞으로 당겨와서 그 다음 무거운 사람으로 비교
        if (people[start] + people[end] > limit):
            answer += 1
            end -= 1

        # 무게 제한을 넘지 않는다면 -> 최대 2명이 타게 됨 (가벼운 사람 + 무거운 사람)
        else:
            answer += 1
            start += 1      # 그 다음 가벼운 사람
            end -= 1        # 그 다음 무거운 사람

    return answer

if __name__ == '__main__':
    print(solution([10, 10, 10, 70, 70], 100))