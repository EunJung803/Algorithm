## 1. product로 모든 조합 구해서 인덱스 찾기 (구질구질 방법)
"""
from itertools import product

def solution(word):
    answer = 0

    alphabet = ['A', 'E', 'I', 'O', 'U']
    product_list = []
    dictionary = []

    for i in range(1, len(alphabet) + 1):
        product_list.append(list(product(alphabet, repeat=i)))
        tmp = list(product(alphabet, repeat=i))

        for j in range(len(tmp)):
            make_word = ''
            for t in range(len(tmp[j])):
                make_word += tmp[j][t]
            dictionary.append(make_word)

    answer = sorted(dictionary).index(word) + 1

    return answer
"""

######################

## 2. DFS로 길이 5 이하의 단어를 순서대로 만들어가면서 인덱스 찾기
answer = 0

def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    ans = []

    def dfs(cnt, w):
        global answer

        if (cnt == 5):
            return

        for i in range(len(alphabet)):
            made_word = w + alphabet[i]
            if(made_word == word):
                answer = len(ans) + 1
            ans.append(made_word)
            dfs(cnt+1, made_word)

    dfs(0, "")

    return answer

print(solution("AAAAE"))