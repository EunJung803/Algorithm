### 순열 풀이법
# from itertools import permutations
#
# def solution(ability):
#     answer = 0
#
#     # 각 종목 대표의 해당 종목에 대한 능력치의 합을 최대화하기
#     # 각 열에서 하나씩 뽑아서 더하기 & 한번 뽑은 행은 뽑을 수 없음 -> 최대값 만들기
#
#     p_ability = list(permutations(ability, len(ability[0])))
#
#     for i in range(len(p_ability)):
#         p_sum = 0
#         for j in range(len(p_ability[i])):
#             p_sum += p_ability[i][j][j]
#         answer = max(answer, p_sum)
#
#     return answer
#

### DFS 풀이법
answer = 0
def DFS(L, s, ability, check):
    global answer
    n = len(ability)  # 학생 수
    m = len(ability[0])  # 종목 개수

    if L == m:
        answer = max(answer, s)  # 능력치 합의 최댓값을 구함
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                DFS(L + 1, s + ability[i][L], ability, check)
                check[i] = 0


def solution(ability):
    global answer
    check = [0] * len(ability)
    DFS(0, 0, ability, check)
    # Level, sum, ability, check
    # L : level (고를 수 있는 학생 수 중 몇 명째 선택한 것인지), sum : 능력치의 합

    return answer

if __name__ == '__main__':
    print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))