def solution(food):
    answer = ''
    left = ''
    right = ''

    for i in range(1, len(food)):   # 물 부분 생략하고 음식 부분부터 for문으로 홀수 -> -1 해서 제일 큰 짝수 만들기 작업
        if (food[i] % 2 != 0):
            food[i] = food[i] - 1

    # enumerate 특징 : enumerate 함수의 두 번째 인수는 시작 값을 지정합니다.
    # 생략한 경우에는 0부터 시작합니다.
    # 시작 값을 지정한 경우는 시작 값부터 값이 증가합니다.
    for i, j in enumerate(food):
        # i는 0, 1, 2, 3 ...
        # j는 food 리스트의 인덱스 0부터 ...
        left += str(i) * (j // 2)   # food[i]는 i번째 음식 수 이므로 1 2 이렇게 있으면 1을 두번 반복해줘야함!

    answer += left  # 물인 0이 나오기 전까지 채우기
    answer += '0'   # 물 부분 채우기

    right += left[::-1]     # 문자열 뒤집기
    answer += right         # 나머지 뒷부분 채우기

    print(answer)
    return answer

if __name__ == '__main__':
    solution([1,3,4,6])
    solution([1,7,1,2])