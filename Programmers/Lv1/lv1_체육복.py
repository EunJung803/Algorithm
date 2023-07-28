def solution(n, lost, reserve):
    # n번 학생은 n-1번이나 n+1번에게만 빌려줄 수 있음
    # 여벌을 가져온 학생 번호가 도난당하면 -> 못빌려줌

    can_gym = []  # 체육 수업에 들어갈 수 있는 학생
    n = n - len(lost)  # 체육복을 안잃어버린 학생 수

    lost = sorted(lost, reverse=True)
    reserve = sorted(reserve, reverse=True)

    # 여벌을 가져온 학생 중 도난 당해서 못빌려주는 학생 찾기
    # 빌려줄 수 있는 학생 배열에서 제거 + 도난 당한 학생 배열에서 제거 -> 못빌려주지만 자기는 수업에 들어갈 수 있으니 can_gym 배열에 추가
    for l in lost:
        if (l in reserve):
            can_gym.append(l)
            reserve[reserve.index(l)] = -1
            lost[lost.index(l)] = -1

    # 빌려줄 수 있는 학생을 찾는다면 -> 체육복을 빌린 학생은 수업 참여 가능하므로 can_gym 배열에 추가 + 빌려주었으니 빌려준 학생은 빌려줄 수 있는 학생 배열에서 제거
    for l in lost:
        if (l + 1 in reserve):
            can_gym.append(l)
            reserve.pop(reserve.index(l + 1))
            # reserve[reserve.index(l + 1)] = -1
        elif (l - 1 in reserve):
            can_gym.append(l)
            reserve.pop(reserve.index(l - 1))
            # reserve[reserve.index(l - 1)] = -1

    answer = n + len(can_gym)

    return answer


if __name__ == '__main__':
    print(solution(24, [12, 13, 16, 17, 19, 20, 21, 22], [1, 22, 16, 18, 9, 10]))       # 19
    print(solution(5, [2, 3, 5], [2, 3, 4]))        # 5
