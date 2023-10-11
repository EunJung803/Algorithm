#import sys
#sys.stdin = open("input.txt", "r")

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
N = int(input())
ans = ""
for i in range(1, N+1):
    if("3" in str(i) or "6" in str(i) or "9" in str(i) ):
        sub_ans = ""
        sub_num = str(i)
        for j in range(len(sub_num)):
            if(sub_num[j] == "3" or sub_num[j] == "6" or sub_num[j] == "9"):
                sub_ans += "-"
        ans += sub_ans
    else:
        ans += str(i)
    if(i < N):
        ans += " "

print(ans)
