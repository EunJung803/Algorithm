def solution(numbers):
    answer = ''

    # 정답 코드
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)    # numbers의 숫자를 str형으로 3번 반복한 값을 기준으로 내림차순 정렬
    for i in numbers:
        answer += str(i)
    answer = str(int(answer))       # 같은 수가 반복되는 정답 케이스가 있다면 걸러주기 (ex. '00' -> 0 -> '0')

    return answer

if __name__ == '__main__':
    print(solution([3, 30, 34, 5, 9]))
    print(solution([0, 0]))
    print(solution([100, 1000]))


### 순열 permutations로 해결하고자 한 코드 -> 시간 초과 발생
# from itertools import permutations
#
# def solution(numbers):
#     answer = ''
#
#     build_num = list(permutations(numbers, len(numbers)))
#     max_num = 0
#
#     for i in range(len(build_num)):
#         make_num = ''
#         for j in range(len(numbers)):
#             make_num += str(build_num[i][j])
#         if(max_num < int(make_num)):
#             max_num = int(make_num)
#
#     answer = str(max_num)
#
#     return answer

### 실패 코드 1
### (dict()으로 설정하니 3번 반복한 후 잘랐을 때 같은 수가 존재한걸 처리할 수 없음)
# num_dict = dict()
#
# for num in numbers:
#     str_num = str(num) * 3
#     num_dict[int(str_num[:3])] = str(num)
#
# print(num_dict)
# ans = list(sorted(num_dict.keys(), reverse=True))
#
# for i in ans:
#     answer += num_dict.get(i)

### 실패 코드 2
### (미완성)
# for num in numbers:
#     if(num < 10):
#         one_len_num.append(num)
#     else:
#         over_len_num.append(num)

# for num in numbers:
#     if (num < 10):
#         one_len_num = num
#     else:
#         over_len_num = num
#
#     if (one_len_num[0] > int(str(over_len_num[0])[0])):
#         ans.append(one_len_num[0])
#
# while (True):
#     for i in range(len(over_len_num)):
#         num_str = str(over_len_num[i])
#         if (int(num_str[0]) <= one_len_num[i]):
#             answer += str(one_len_num[0])
#             one_len_num.pop(0)