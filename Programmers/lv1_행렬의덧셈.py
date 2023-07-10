def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        sub_array = []
        for j in range(len(arr1[i])):
            sum = arr1[i][j] + arr2[i][j]
            sub_array.append(sum)
        answer.append(sub_array)

    return answer

if __name__ == '__main__':
    print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
    print(solution([[1],[2]], [[3],[4]]))