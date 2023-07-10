def solution(arr):
    answer = []

    # [10]인 경우
    if (arr[0] == 10 and len(arr) == 1):
        answer.append(-1)
        return answer

    # [10]이 아니라면 제일 작은 수 제거하기 시작
    sorted_arr = sorted(arr)  # arr 정렬 -> 첫번째 인덱스가 제일 작은 수일 것

    # arr에서 제일 작은 수의 위치를 찾아서 pop으로 제거
    for i in range(len(arr)):
        if (arr[i] == sorted_arr[0]):
            arr.pop(i)
            break

    answer = arr

    return answer

if __name__ == '__main__':
    print(solution([4,3,2,1,]))
    print(solution([10]))