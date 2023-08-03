def solution(arr1, arr2):
    answer = []

    mul = 0
    sub = []

    for n in arr1:
        for i in range(len(arr2[0])):
            for j in range(len(n)):
                mul += n[j] * arr2[j][i]
            sub.append(mul)
            mul = 0
        answer.append(sub)
        sub = []

    return answer


if __name__ == '__main__':
    print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
    print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
    print(solution([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]))       # [[14, 32], [32, 77]]
