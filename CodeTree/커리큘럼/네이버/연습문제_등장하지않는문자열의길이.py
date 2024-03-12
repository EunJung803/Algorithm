N = int(input())
str_input = input()
str_list = list(str_input)

checked = set()

double = []

cnt = 1
ans = 0

for i in range(N):
    for j in range(i, N):
        sub_str = str_input[i:j+1]      # 현재 위치에서 만들 수 있는 모든 부분수열 만들기

        if(sub_str not in checked):     # 해당 부분수열이 한번도 나오지 않았던 것이라면 -> 다음 비교를 위해 checked 집합에 추가
            checked.add(sub_str)
        else:                           # 해당 부분수열이 앞전에 이미 나온 것이라면 -> 길이값 업데이트
            ans = max(ans, len(sub_str)+1)

print(ans)
