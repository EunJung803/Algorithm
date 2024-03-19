from collections import deque

F, S, G, U, D = map(int, input().split())

""""
G에 가야함
총 F층으로 이루어져있음
현재 나는 S층

엘베 버튼 U : U층 위로 이동
엘베 버튼 D : D층 아래로 이동
"""

visited = [0 for _ in range(F+1)]

q = deque()
q.append([S, 0])
visited[S] = 1

flag = False

while(q):
    curr = q.popleft()
    # print(curr)
    curr_floor = curr[0]
    curr_cnt = curr[1]

    if(curr_floor == G):
        flag = True
        print(curr_cnt)
        break

    next_floor1 = curr_floor + U
    next_floor2 = curr_floor - D
    if(0 < next_floor1 <= F):
        if(visited[next_floor1] == 0):
            q.append([next_floor1, curr_cnt + 1])
            visited[next_floor1] = 1
    if(0 < next_floor2 <= F):
        if(visited[next_floor2] == 0):
            q.append([next_floor2, curr_cnt + 1])
            visited[next_floor2] = 1

if(flag == False):
    print("use the stairs")