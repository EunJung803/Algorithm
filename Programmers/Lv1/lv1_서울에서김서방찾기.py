def solution(seoul):
    answer = ''

    for i in range(len(seoul)):
        if(seoul[i] == "Kim"):
            answer = "김서방은 {index}에 있다".format(index = i)   # 파이썬 문자열 형식화 1 - format 사용
            # answer = f"김서방은 {i}에 있다"                        # 파이썬 문자열 형식화 2 - f 사용

    return answer


if __name__ == '__main__':
    print(solution(["Jane", "Kim"]))