from collections import deque


def solution(priorities, location):
    answer = 0

    q = deque()

    for i in range(len(priorities)):
        q.append([priorities[i], i])

    ans = []
    while (q):
        flag = True
        # 1. 프로세스 꺼내기
        curr = q.popleft()
        process = curr[0]
        idx = curr[1]

        # 2. 자신보다 우선순위가 높은게 아직 큐에 있다면 -> 꺼낸 프로세스 다시 집어넣기
        for i in range(len(q)):
            if (process < q[i][0]):
                q.append([process, idx])
                flag = False
                break

        # 3. 그런 프로세스가 없다면 실행
        if (flag):
            ans.append([process, idx])

    # 정답 추출
    for i in range(len(ans)):
        if (ans[i][1] == location):
            answer = i + 1
            break

    return answer