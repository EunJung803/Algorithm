from itertools import combinations

N = int(input())
team_list = [list(map(int, input().split())) for _ in range(N)]

num_list = [i for i in range(N)]

combi = list(combinations(num_list, N//2))

ans = N*N*N

for i in range(len(combi)//2):
    s_team = 0
    l_team = 0

    t1 = combi[i]
    t2 = combi[len(combi) - 1 - i]

    t1_combi = list(combinations(t1, 2))
    t2_combi = list(combinations(t2, 2))

    for j in range(len(t1_combi)):
        s_team += team_list[t1_combi[j][0]][t1_combi[j][1]]
        s_team += team_list[t1_combi[j][1]][t1_combi[j][0]]

        l_team += team_list[t2_combi[j][0]][t2_combi[j][1]]
        l_team += team_list[t2_combi[j][1]][t2_combi[j][0]]

    ans = min(ans, abs(s_team - l_team))

print(ans)