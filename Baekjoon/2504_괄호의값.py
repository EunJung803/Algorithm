input_str = input()

arr = []    # 괄호를 넣어가면서 계산한 값을 담을 배열

open_cnt = 0    # 여는 괄호 개수 카운트
close_cnt = 0   # 닫는 괄호 개수 카운트

for i in range(len(input_str)):
    # 괄호의 시작인 값이면 -> 배열에 우선 넣어주기
    if(input_str[i] == '(' or input_str[i] == '['):
        arr.append(input_str[i])
        open_cnt += 1

    # 괄호의 끝인 값이면 -> 짝이 지어지는지 확인
    else:
        close_cnt += 1
        # 배열이 비어있는데 닫는 괄호가 들어오면 잘못된 괄호열
        if(len(arr) == 0):
            break

        # () 짝지어짐
        if(input_str[i] == ')' and arr[-1] == '('):
            arr.pop(-1)
            arr.append(2)   # () 값인 2 넣어주기
            if (len(arr) >= 2 and isinstance(arr[-2], int)):    # 그 전에 계산된 수가 들어가있다면 더해서 배열 업데이트
                sum_tmp = arr[-2] + arr[-1]
                arr.pop(-1)
                arr.pop(-1)
                arr.append(sum_tmp)
            continue
        # [] 짝지어짐
        if (input_str[i] == ']' and arr[-1] == '['):
            arr.pop(-1)
            arr.append(3)   # [] 의 값인 3 넣어주기
            if (len(arr) >= 2 and isinstance(arr[-2], int)):    # 그 전에 계산된 수가 들어가있다면 더해서 배열 업데이트
                sum_tmp = arr[-2] + arr[-1]
                arr.pop(-1)
                arr.pop(-1)
                arr.append(sum_tmp)
            continue
        # ( X ) 의 경우
        elif(len(arr) >= 2 and input_str[i] == ')' and arr[-2] == '('):
            if (isinstance(arr[-1], int)):
                tmp = arr[-1] * 2
                arr.pop(-1)
                arr.pop(-1)
                arr.append(tmp)
                if(len(arr) >= 2 and isinstance(arr[-2], int)):
                    sum_tmp = arr[-2] + tmp
                    arr.pop(-1)
                    arr.pop(-1)
                    arr.append(sum_tmp)
            continue
        # [ X ] 의 경우
        elif(len(arr) >= 2 and input_str[i] == ']' and arr[-2] == '['):
            if(isinstance(arr[-1], int)):
                tmp = arr[-1] * 3
                arr.pop(-1)
                arr.pop(-1)
                arr.append(tmp)
                if(len(arr) >= 2 and isinstance(arr[-2], int)):
                    sum_tmp = arr[-2] + tmp
                    arr.pop(-1)
                    arr.pop(-1)
                    arr.append(sum_tmp)
            continue
#
#     print(arr)
#     print("==")
#
# print(arr)

# 정답 출력
if(len(arr) != 1 or open_cnt != close_cnt):
    print(0)
else:
    print(arr[0])