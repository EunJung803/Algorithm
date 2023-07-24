from collections import Counter

def solution(X, Y):
    answer = ''

    X = Counter(X)
    Y = Counter(Y)

    print(X)
    print(Y)

    for i in range(9, -1, -1):      # 9 ~ 0 까지 순회
        if(X[str(i)] != 0 and Y[str(i)] != 0):      # 만약 둘 다 같은 숫자가 1개라도 존재하고 있다면
            can_make_couple = min(X[str(i)], Y[str(i)])     # 짝꿍을 만들 수 있는 최대 횟수를 구하기
            answer += str(i) * can_make_couple              # 해당 숫자를 짝꿍으로 만들 수 있는 개수만큼 짝꿍 만들어서 정답에 추가

    if (len(answer) == 0):
        return "-1"

    if(answer[0] == "0"):
        return "0"

    return answer

if __name__ == '__main__':
    print(solution("100", "2345"))
    print(solution("100", "203045"))
    print(solution("100", "123450"))
    print(solution("12321", "42531"))
    print(solution("5525", "1255"))