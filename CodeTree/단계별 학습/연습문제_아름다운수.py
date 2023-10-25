# n = int(input())
n = 3

arr = []

ans = 0
b_num = ''

def check_beautiful():
    c_2 = b_num.count('2')
    c_3 = b_num.count('3')
    c_4 = b_num.count('4')

    if (c_2 % 2 == 0 and c_3 % 3 == 0 and c_4 % 4 == 0):
        i = 0

        while(i < n):
            check_num = int(b_num[i])   # 검사해야하는 시작 번호
            for j in range(i, i + check_num):       # 해당 번호가 그 번호의 길이만큼 연속하는지 확인
                if(int(b_num[j]) != check_num):     # 연속으로 존재하지 않으면 False
                    return False
            i += check_num      # 그 다음 번호를 비교할 때에는 시작번호로 검사한 만큼 건너뛰고 검사를 시작해야함

    else:       # 2, 3, 4의 개수가 각각의 배수 갯수만큼 존재하지 않는다면 아름다운 수 X
        return False

    # 모든 검사를 통과하면 아름다운 수
    return True


def beautiful_num(num):     # 1,2,3,4를 n의 길이만큼 만들 수 있는 모든 숫자를 만드는 함수
    global b_num    # 아름다운 수를 담을 문자열
    global ans

    if (num == n):  # 종료 조건
        if (check_beautiful()):
            # arr.append(b_num)
            ans += 1
        return

    for i in range(1, 5):  # 1 ~ 4로만 구성
        b_num += str(i)
        beautiful_num(num + 1)
        b_num = b_num[:-1]

    return


## 메인 실행
beautiful_num(0)  # n의 길이만큼 아름다운 수의 후보를 만들어내기
# print(arr)
print(ans)