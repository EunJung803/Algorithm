# from collections import deque
#
# # 두 단어의 알파벳 개수 차이를 체크하는 함수
# def check_diff(word1, word2):
#     cnt = 0
#     for i in range(len(word1)):
#         if (word1[i] != word2[i]):
#             cnt += 1
#         if (cnt >= 2):  # 알파벳이 2개 이상 다르면 변환 불가
#             break
#     return cnt
#
#
# def solution(begin, target, words):
#     answer = 0
#     check = [False for i in range(len(words))]
#
#     if (target not in words):
#         return 0
#
#     q = deque()
#     q.append(begin)
#
#     while (q):
#         answer += 1
#         for k in range(len(q)):     # 큐에 있는 변환 가능 후보들을 하나씩 뽑기
#             word = q.popleft()
#
#             # 그 다음으로 변환 가능한 단어 찾기
#             for i in range(len(words)):
#                 if(check[i] == False and check_diff(word, words[i]) == 1):      # 이전에 변환한 기록이 없고, 현재 단어에서 알파벳 차이가 딱 1개만 난다면
#                     q.append(words[i])      # 변환 가능하므로 -> 큐에 삽입
#                     check[i] = True         # 변환 기록 체크
#                     if(words[i] == target):     # 현재 변환 가능한 단어가 만약 target이라면, 지금 횟수가 최소 변환 횟수이므로 정답으로 출력
#                         return answer
#
#     return answer


# 230319 풀이
from collections import deque

def solution(begin, target, words):
    answer = 0

    # target이 words에 없어서 변환할 수 없는 경우
    if (target not in words):
        return 0

    visited = [0 for _ in range(len(words))]

    # 두 단어의 차이나는 알파벳 수 반환
    def word_sub(w1, w2):
        cnt = 0
        for i in range(len(w1)):
            if (w1[i] != w2[i]):
                cnt += 1
        return cnt

    # BFS 탐색으로 다음에 변환할 수 있는거 찾아가기
    def bfs(q):
        while (q):
            curr = q.popleft()
            curr_w = curr[0]
            curr_cnt = curr[1]

            if (curr_w == target):
                return curr_cnt

            for i in range(len(words)):
                ws = word_sub(curr_w, words[i])
                if (visited[i] == 0 and ws == 1):
                    q.append([words[i], curr_cnt + 1, i])
                    visited[i] = 1

        return curr_cnt

    q = deque()

    for i in range(len(words)):
        # begin이랑 1개의 알파벳 차이만 나서 변환 가능한거 우선 큐에 다 넣기
        if (word_sub(begin, words[i]) == 1):
            q.append([words[i], 1, i])
            visited[i] = 1

    # BFS 탐색
    answer = bfs(q)

    return answer

if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))   # 4