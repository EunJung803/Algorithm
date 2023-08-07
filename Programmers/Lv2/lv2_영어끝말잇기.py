def solution(n, words):
    answer = []

    # 1 -> 2 -> 3 -> 1 -> 2 ... 돌아가면서 진행
    # 1. 앞사람 단어의 끝나는 글자로 시작하지 못하면 X
    # 2. 이전에 등장한 단어 사용 X
    # 3. 한글자 단어 X
    # [탈락하는 사람의 번호, 자신이 몇번째 차례에 탈락하게 된지]

    pass_word = []

    for i, w in enumerate(words):
        # 첫번째 단어가 아닐 때 검사할 부분 (위 주석의 1, 2번 조건)
        if(i > 0):
            if(w[0] != words[i-1][-1]):     # 1번 조건
                out = (i % n) + 1
                out_time = (i // n) + 1
                answer.append(out)
                answer.append(out_time)
                break
            if(w in pass_word):             # 2번 조건
                out = (i % n) + 1
                out_time = (i // n) + 1
                answer.append(out)
                answer.append(out_time)
                break
        # 첫번째 단어도 검사해야하는 부분 (3번 조건)
        if(len(w) == 1):                    # 3번 조건
            out = (i % n) + 1
            out_time = (i // n) + 1
            answer.append(out)
            answer.append(out_time)
            break

        pass_word.append(w)     # 모든 검사에서 통과한 단어는 pass_word에 넣어서 다음 단어를 검사할 때 사용

    if(len(answer) == 0):   # 모든 조건에서 걸리지 않고 나왔을 때, 탈락자는 없다
        return [0, 0]

    return answer

if __name__ == '__main__':
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))