def solution(arr):
    answer = 0

    num1 = arr[0]   # 초기 num1은 배열의 첫번째 값
    for i in range(1, len(arr)):
        num2 = arr[i]
        # num1과 num2의 최소공배수를 구하는 부분
        for n in range(max(num1, num2), num1 * num2 + 1):
            if (n % num1 == 0 and n % num2 == 0):
                num1 = n    # 현재 num1과 num2의 최소공배수를 다음 num2와 비교해서 또 그 둘의 최소공배수를 계속 구해야하기 때문에 num1 업데이트
                break

    answer = num1   # 마지막으로 구해진 최소공배수가 배열에 있는 모든 N개의 값에 대한 최소공배수

    return answer