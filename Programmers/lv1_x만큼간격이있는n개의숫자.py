def solution(x, n):
    answer = []

    if(x == 0):
        for i in range(x, n):
            answer.append(x)

    if(x > 0):
        for i in range(x, x*n+1, x):
            answer.append(i)
    if(x < 0):
        for i in range(x, x*n-1, x):
            answer.append(i)

    print(answer)
    return answer

if __name__ == '__main__':
    solution(2, 5)
    solution(4, 3)
    solution(0, 2)