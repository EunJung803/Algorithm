from itertools import permutations

# 소수인지 판별하는 함수
def prime_check(num):
    if (num <= 1):
        return False
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            return False
    return True

def solution(numbers):
    answer = 0

    prime_list = set()      # 만들어진 소수를 담을 set (중복 제거를 위해)

    for i in range(1, len(numbers) + 1):
        per = list(set(permutations(numbers, i)))   # numbers 문자열에서 i개를 뽑아서 만들 수 있는 순열 생성 (set으로 감싸서 중복을 제거하고 -> list로 감싸서 접근에 용이하게 하기)

        # 해당 순열 리스트를 돌면서 숫자로 하나씩 만든 뒤 -> 소수인지 아닌지 판별하기
        for j in range(len(per)):
            make_num = ''

            for n in range(len(per[j])):
                make_num += per[j][n]               # 쪼개진 문자를 붙여서 하나의 숫자르 담은 문자열 만들기
            flag = prime_check(int(make_num))       # 소수인지 판별
            if (flag):      # 소수라면
                prime_list.add(int(make_num))       # set에 추가

    answer = len(prime_list)    # 정답은 prime_list에 담겨있는 소수들의 개수

    return answer

if __name__ == '__main__':
    print(solution("17"))
    print(solution("011"))