from collections import deque

# 두 단어의 알파벳 개수 차이를 체크하는 함수
def check_diff(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if (word1[i] != word2[i]):
            cnt += 1
        if (cnt >= 2):  # 알파벳이 2개 이상 다르면 변환 불가
            break
    return cnt


def solution(begin, target, words):
    answer = 0
    check = [False for i in range(len(words))]

    if (target not in words):
        return 0

    q = deque()
    q.append(begin)

    while (q):
        answer += 1
        for k in range(len(q)):     # 큐에 있는 변환 가능 후보들을 하나씩 뽑기
            word = q.popleft()

            # 그 다음으로 변환 가능한 단어 찾기
            for i in range(len(words)):
                if(check[i] == False and check_diff(word, words[i]) == 1):      # 이전에 변환한 기록이 없고, 현재 단어에서 알파벳 차이가 딱 1개만 난다면
                    q.append(words[i])      # 변환 가능하므로 -> 큐에 삽입
                    check[i] = True         # 변환 기록 체크
                    if(words[i] == target):     # 현재 변환 가능한 단어가 만약 target이라면, 지금 횟수가 최소 변환 횟수이므로 정답으로 출력
                        return answer

    return answer

if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))   # 4