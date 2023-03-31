"""
Question1: The cost of a string

Your task is to create a string S considering lowercase English alphabets.
You are given an array A of size 26 where A[i] denotes the cost of using the ith Alphabet (consider 1-based indexing).
Find lexicographically the largest string S that can be created such that the cost of building the string is exactly W.
For example, ‘abc’ is lexicographically smaller than ‘abcd’.

"""

# 가장 뒤에 있는데 W보다는 작은 cost 값 찾기
def finding_cost(W, alphabets):
    for i in range(len(alphabets) - 1, 0, -1):
        if (W < alphabets[i]):
            pass
        else:
            cost = alphabets[i]
            index.append(i)
            break
    return cost

# 정답 문자열 찾기
def getting_ans(W):
    # answer = []
    for letter in index:
        ans_letter = chr(letter + 97)
        # answer.append(ans_letter)
        print(ans_letter, end="")

# 핵심 파트
max_num = 0
my_letter = 0
index = []

# input 받기
test_num = int(input())
# test num 만큼 돌리기
for i in range(test_num):
    alphabets = list(map(int, input().split()))     # cost들 인풋받기
    W = int(input())    # W 인풋받기

    # 조건 = W보다는 작아야함 -> 최대한 맨 마지막 인덱스여야함 -> W - cost < 마지막 인덱스의 값 이면, 다른 cost 값을 찾기 (인덱스 옮기기)

    cost = finding_cost(W, alphabets)
    # print("current cost", cost)
    while (W >= cost):
        W = W - cost
        # print("W : ", W)

        if (W == 0):
            getting_ans(W)
            break

        cost = finding_cost(W, alphabets)
        # print("new cost", cost)
