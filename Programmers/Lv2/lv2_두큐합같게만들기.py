from collections import deque

def solution(queue1, queue2):
    answer = 0

    q_1 = deque(queue1)
    q_2 = deque(queue2)

    s_1 = sum(queue1)
    s_2 = sum(queue2)

    check_odd = (s_1 + s_2) % 2
    if (check_odd != 0):  # 각 큐가 만들어야 하는 합이 소수인 경우는 불가능
        return -1

    limit = len(queue1) * 3     # 최대 연산 횟수 (시간복잡도를 위한 조건)
    while (s_1 != s_2):
        if (len(q_1) == 0 or len(q_2) == 0):
            return -1
        if(answer >= limit):
            return -1

        if(s_1 > s_2):
            pop_num = q_1.popleft()
            q_2.append(pop_num)

            s_2 += pop_num
            s_1 -= pop_num

            answer += 1
        elif(s_1 < s_2):
            pop_num = q_2.popleft()
            q_1.append(pop_num)

            s_1 += pop_num
            s_2 -= pop_num

            answer += 1

    return answer

if __name__ == '__main__':
    print(solution([1,4], [4,8]))       # -1
    print(solution([2,4,6], [1,3,5]))   # -1
    print(solution([1,1], [1,5]))       # -1
    print(solution([8,8], [2,8]))       # -1