def solution(n):
    answer = ''
    for i in range(n):
        if(i % 2 == 0):
            answer += '수'
        else:
            answer += '박'

    return answer

if __name__ == '__main__':
    print(solution(4))
    print(solution(3))
