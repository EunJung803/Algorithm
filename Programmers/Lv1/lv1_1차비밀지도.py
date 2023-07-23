def decode_to_binary(a, n):     # 10진수 -> 2진수
    binary = ''
    while(a > 0):       # 2진수 구하기
        div = a // 2
        left = a % 2
        binary += str(left)
        a = div

    ans_binary = binary[::-1]   # 왼쪽 -> 오른쪽으로 집어넣어주었기 때문에 정답인 2진수를 얻기 위해서 한번 뒤집어주기

    if(len(ans_binary) < n):    # 만약 n의 길이보다 짧다면, 왼쪽에 부족한 길이만큼 0을 추가로 붙여주기
        ans_binary = ('0' * (n - len(binary))) + ans_binary

    return ans_binary

def solution(n, arr1, arr2):
    answer = []

    # "지도 1 벽" or "지도 2 벽" == 벽
    # "지도 1 공백" and "지도 2 공백" = 공백

    # 벽 == 1, 공백 == 0
    # 벽 == '#', 공백 == ' '

    # TODO
    ## 각 배열의 값을 이진법으로 변환 (9 -> 01001)
    ## 두 배열 다 공백인건 공백, 두 배열 중 하나만 벽이면 벽 -> 최종 배열 만들기
    ## 정답 출력하기

    # 이진법 변환하기
    for i in range(n):
        arr1[i] = decode_to_binary(arr1[i], n)
        arr2[i] = decode_to_binary(arr2[i], n)

        # 둘 다 0이면 -> 공백
        # 둘 중 하나라도 1이면 -> 벽
        ans = ''
        for j in range(n):
            if(arr1[i][j] == '0' and arr2[i][j] == '0'):    # 공백
                ans += ' '
            if (arr1[i][j] == '1' or arr2[i][j] == '1'):    # 벽
                ans += '#'
        answer.append(ans)

    # print(arr1)
    # print(arr2)

    return answer

if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))