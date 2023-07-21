def solution(ingredient):
    answer = 0

    # 빵 야채 고기 빵
    # 1 2 3 1

    hamburger = [1, 2, 3, 1]    # 햄버거 순서
    making = []
    for i in range(len(ingredient)):
        making.append(ingredient[i])        # making 배열에 쌓인 재료들을 하나씩 넣으면서 햄버거를 만들 수 있는지 판단

        length = len(making)
        if (making[length-4:] == hamburger):    # 햄버거를 만들 수 있는 재료 순서로 쌓이면 -> 햄버거를 하나 만들었으니 answer += 1
            answer += 1
            making.pop(length-4)                # 햄버거를 만들고 나서 소진한 재로는 제거해주기
            making.pop(length-4)
            making.pop(length-4)
            making.pop(length-4)

    return answer

if __name__ == '__main__':
    print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
    print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))