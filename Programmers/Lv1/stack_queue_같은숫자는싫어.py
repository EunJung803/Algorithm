def solution(arr):
    answer = []

    for i in range(len(arr) - 1):
        if (arr[i] != arr[i + 1]):  # 앞 뒤 값이 다르면
            answer.append(arr[i])   # 맨 앞의 값을 넣어주고

    answer.append(arr[-1])  # 마지막에 비교 못한 요소를 추가로 넣어준다
    return answer