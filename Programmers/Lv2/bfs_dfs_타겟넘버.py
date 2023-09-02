### DFS
def solution(numbers, target):
    answer = 0

    def dfs(index, numbers_sum):
        if (index == len(numbers)):
            if (numbers_sum == target):
                nonlocal answer
                answer += 1
            return

        dfs(index + 1, numbers_sum + numbers[index])
        dfs(index + 1, numbers_sum - numbers[index])

    dfs(0, 0)

    return answer

### BFS
# def solution(numbers, target):
#     answer = 0
#     queue = [[numbers[0],0], [-1*numbers[0],0]]
#     n = len(numbers)
#     while queue:
#         temp, idx = queue.pop()
#         idx += 1
#         if idx < n:
#             queue.append([temp+numbers[idx], idx])
#             queue.append([temp-numbers[idx], idx])
#         else:
#             if temp == target:
#                 answer += 1
#     return answer

if __name__ == '__main__':
    print(solution([1,1,1,1,1], 3))