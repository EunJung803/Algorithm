import math

input_num = list(map(int, input().split()))
a = input_num[0]
b = input_num[1]

print(math.gcd(a, b))               # 최대공약수
print(int(a * b / math.gcd(a, b)))  # 최소공배수

