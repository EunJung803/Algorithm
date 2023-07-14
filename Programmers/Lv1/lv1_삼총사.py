def solution(number):
    answer = 0

    for x in range(len(number)):
        for y in range(x+1, len(number)):
            for z in range(y+1, len(number)):
                sum = 0
                sum += number[x] + number[y] + number[z]
                if(sum == 0):
                    answer += 1

    return answer

if __name__ == '__main__':
    print(solution([-2, 3, 0, 2, -5]))
    print(solution([-3, -2, -1, 0, 1, 2, 3]))
    print(solution([-1, 1, -1, 1]))