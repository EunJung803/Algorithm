N, M, D, S = map(int, input().split())
D_list = [list(map(int, input().split())) for _ in range(D)]
S_list = [list(map(int, input().split())) for _ in range(S)]

med = 0

check_human = [False for _ in range(N)]     # 먹고 아픈 사람 + 아플 가능성이 있는 사람 체크를 위한 리스트

cheese = []
for i in range(S):
    sick_person = S_list[i][0]
    t = S_list[i][1]

    for j in range(D):
        if(D_list[j][0] == sick_person and D_list[j][2] < t and check_human[sick_person - 1] == False):     # 1. 치즈를 먹은 리스트에서 아픈 사람을 발견하면
            check_human[sick_person - 1] = True

            # 2. 그 아픈 사람이 먹은 상했을 가능성이 있는 모든 치즈 찾아서 담아두기
            bad_cheese = []
            bad_cheese.append(D_list[j][1])
            for d in range(D):
                if(D_list[d][0] == sick_person and D_list[d][2] < t and D_list[d][1] not in bad_cheese):
                    bad_cheese.append(D_list[d][1])
            print(bad_cheese)

            # 3. 모든 아픈사람이 먹은 치즈 찾아내기 (교집합)
            if(len(cheese) == 0):
                cheese = bad_cheese
            else:
                cheese = list(set(cheese) & set(bad_cheese))

            # print(cheese)


# 4. 상한 치즈들을 모두 찾았다면 -> 그 상한 치즈를 먹어서 같이 아플 가능성이 있는 사람 체크
for i in range(D):
    if(check_human[D_list[i][0] - 1] == False and D_list[i][1] in cheese):
        check_human[D_list[i][0] - 1] = True


# print(check_human)
print(check_human.count(True))      # 정답 출력