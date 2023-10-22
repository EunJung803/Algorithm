import heapq

def solution(n, works):
    answer = 0

    if n >= sum(works):     # 모든 작업을 퇴근까지 남은 시간 안에 다 끝낼 수 있는 경우
        return 0

    works = [-w for w in works]     # works 배열의 모든 값을 음수로 만들어줘서
    heapq.heapify(works)            # 배열 -> 힙 으로 바꿀때 최대 힙을 사용할 수 있도록 함 (heapify == 배열을 힙으로 바꾸는 메서드)

    for _ in range(n):
        i = heapq.heappop(works)    # 힙에서 하나씩 뽑아서
        i += 1      # 1을 빼주는 작업 (음수 + 1 -> 절댓값으로 보면 1이 줄어듦)
        heapq.heappush(works, i)    # 다시 힙에 넣어서 정렬되도록

    # 정답 출력을 위해 각 원소의 제곱을 더해주기
    for i in range(len(works)):
        answer += ((-1) * works[i]) ** 2

    return answer


# from heapq import heappush, heappop
#
# def solution(n, works):
#     answer = 0
#
#     # 피로도 += 남은 일의 작업량 ** 2
#     # N시간 동안 피로도 최소화
#     ## TODO : 매번의 최댓값을 구한다 -> 해당 최댓값에서 -1씩 해줌
#
#     work_heap = []
#     for num in works:
#         heappush(work_heap, -num)
#
#     while (n > 0):
#         to_sub = (-1) * heappop(work_heap)
#         if (to_sub == 0):
#             break
#         elif (to_sub < n):  # 최대값이 n보다 작은 경우, n을 한번에 줄이기
#             n -= to_sub
#         elif (to_sub >= n):  # 1씩 빼주는 경우
#             to_sub -= 1
#             n -= 1
#             heappush(work_heap, -to_sub)
#
#     for i in range(len(work_heap)):
#         answer += ((-1) * work_heap[i]) ** 2
#
#     return answer


if __name__ == '__main__':
    # print(solution(4, [4, 3, 3]))
    # print(solution(999, [100, 800, 55, 45]))        # 1
    # print(solution(9, [1,1,1]))     # 0
    print(solution(99, [2, 15, 22, 55, 55]))      # 580
    

#####

"""
def solution(n, works):
    answer = 0
    
    # 피로도 += 남은 일의 작업량 ** 2
    # N시간 동안 피로도 최소화
    
    works = sorted(works, reverse = True)
        
    # 매번의 최댓값을 구한다 -> 해당 최댓값에서 -1씩 해줌
    
    while(n > 0):
        max_index = works.index(max(works))
        to_sub = works[max_index]
        if(to_sub == 0):
            break
        if(sum(works) == to_sub and n < to_sub):   # 모두가 0이고 요소가 하나 남았을 때
            works[max_index] = abs(to_sub - n)
            break
        elif(to_sub < n):   # 최대값이 n보다 작은 경우, n을 한번에 줄이기
            works[max_index] = 0
            n -= to_sub
        elif(to_sub >= n):  # 1씩 빼주는 경우
            works[max_index] -= 1
            n -= 1
        # print(n, works)
        
    # print(works)
    
    for i in range(len(works)):
        answer += works[i] ** 2
    
    return answer
"""
