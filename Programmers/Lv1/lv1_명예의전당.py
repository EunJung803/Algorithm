def solution(k, score):
    answer = []

    mj = []  # 명예의 전당

    for i in range(len(score)):
        if (i + 1 <= k):            # k일 전이라면 계속 명예의 전당에 들어가게 되므로 우선 계속 넣는다
            mj.append(score[i])
            mj.sort()
            answer.append(mj[0])
        else:   # k일 이후
            if (mj[0] < score[i]):  # 명예의 전당에 들어갈만큼의 점수가 나온다면 -> 가장 최하점을 밀어내고 현재 점수가 들어간 뒤, 그 중 최하점 발표
                mj.pop(0)
                mj.append(score[i])
                mj.sort()
                answer.append(mj[0])
            else:
                answer.append(mj[0])

    return answer