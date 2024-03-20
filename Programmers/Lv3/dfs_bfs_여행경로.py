## 이전 풀이
"""
# from collections import deque
from collections import defaultdict

def solution(tickets):
    answer = ["ICN"]
    d = defaultdict(list)   # 리스트를 value로 갖는 딕셔너리 생성

    # key는 출발지, value에는 도착지들 리스트
    for ticket in tickets:
        d[ticket[0]].append(ticket[1])

    # 알파벳 내림차순 정렬
    # ["SFO", "ATL"] 이런 식으로 정렬되기 때문에 나중에 d[top].pop() 으로 알파벳 순서가 앞서는 나라부터 탐색할 수 있음
    for key in d.keys():
        d[key].sort(reverse = True)

    stack = ["ICN"]     # ICN 부터 시작
    path = []

    while stack:
        top = stack[-1]

        if not d[top] or len(d[top]) == 0:  # value가 존재하지 않거나 해당 나라가 출발지인 티켓이 없다면 stack.pop() 해서 path에 넣어준다
            path.append(stack.pop())

        else:
            stack.append(d[top].pop())      # 가장 마지막에 있는 value를 (알파벳 순서가 앞서는 나라) pop해서 stack에 넣어준다

    return path[::-1]   # path를 뒤집어주면 정답
"""

## DFS 다른 방법
"""
def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes

    # 스택을 사용한 DFS
    def dfs():
        stack = ["ICN"]
        path = []  # 가려고하는 경로를 저장하는 변수
        while len(stack) > 0:  # stack이 비어있을 때까지
            top = stack[-1]
            # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    answer = dfs()
    return answer
"""

## BFS 실패 코드
"""
def solution(tickets):
    answer = []

    # 시작 공항 담고 -> 도착 공항 담고 -> 도착 공항이 시작 공항이 됨 (찾기)

    # airport_list = []
    # for i in range(len(tickets)):
    #     for j in range(2):
    #         if(tickets[i][j] not in airport_list):
    #             airport_list.append(tickets[i][j])
    # print(airport_list)
    #
    # q = deque()
    #
    # route = []
    # ans = []
    #
    # for i in range(len(tickets)):
    #     depart = tickets[i][0]
    #     if(depart == "ICN"):
    #         q.append(depart)
    #
    #     while(q):
    #         current = q.popleft()
    #         for j in range(len(tickets)):
    #             if(tickets[j][0] == current):
    #                 route.append(current)
    #                 arrive = tickets[j][1]
    #                 q.append(arrive)
    #     if(route):
    #         route.append(current)
    #         ans.append(route)
    #         route = []
    #
    # print(ans)

    return answer
"""

## 240320 풀이
"""
from collections import defaultdict

def solution(tickets):
    answer = []

    graph = defaultdict(list)

    for i in range(len(tickets)):
        graph[tickets[i][0]].append(tickets[i][1])
        graph[tickets[i][0]].sort()

    print(graph)

    def dfs(depart, arrive, route):
        route.append(depart)
        print(visited)

        if (visited.count(1) == len(visited)):
            route.append(arrive)
            return route

        for node in graph[arrive]:
            if ([arrive, node] not in tickets):
                return 0
            if ([arrive, node] in visited and [arrive, node] in tickets):
                idx = visited.index([arrive, node])
                if (visited[idx] != 1):
                    visited[idx] = 1
                    dfs(arrive, node, route)

        return route

    total_ans = []
    for i in range(len(tickets)):
        ans = []

        # tickets를 visited에 복사
        visited = []
        for j in range(len(tickets)):
            visited.append(tickets[j])

        # ICN으로 시작하면 해당 티켓부터 사용해서 탐색 시작
        if (tickets[i][0] == "ICN"):
            visited[i] = 1

            ans = dfs(tickets[i][0], tickets[i][1], [])

            print(ans)

            if (visited.count(1) == len(visited) and ans != 0):
                total_ans.append(ans)
            print("==")

    print(total_ans)
    if (total_ans):
        total_ans.sort()
        answer = total_ans[0]

    # # BFS
    # q = deque()
    # 
    # def bfs(q):
    #     route = []
    #     while(q):
    #         curr = q.popleft()
    #         depart = curr[0]
    #         arrive = curr[1]
    # 
    #         # if(depart == "ICN" and len(route) == 0):
    #         route.append(depart)
    #         route.append(arrive)
    # 
    #         for node in graph[arrive]:
    #             if([arrive, node] in tickets):
    #                 idx = tickets.index([arrive, node])
    #                 if(visited[idx] != 1):
    #                     q.append([arrive, node])
    #                     print([arrive, node])
    #                     visited[idx] = 1
    #     return route
    # 
    # total = []
    # for i in range(len(tickets)):
    #     ans = []
    #     # visited = [0 for _ in range(len(tickets))]
    #     visited = []
    #     for j in range(len(tickets)):
    #         visited.append(tickets[j])
    #     if(tickets[i][0] == "ICN"):
    #         q.append(tickets[i])      # ["ICN", "SFO"], i=0
    #         visited[i] = 1
    # 
    #         ans = bfs(q)
    # 
    #     if(ans):
    #         total.append(ans)
    # 
    # 
    # print(total)
    # total.sort()
    # print(total)
    # answer = total[0]

    return answer
"""
"""
from collections import defaultdict


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    for i in range(len(tickets)):
        graph[tickets[i][0]].append(tickets[i][1])
        graph[tickets[i][0]].sort()

    # print(graph)

    def dfs(depart, arrive, route):
        route.append(depart)
        # print(visited)

        if (visited.count(1) == len(visited)):
            route.append(arrive)
            return route

        for node in graph[arrive]:
            if ([arrive, node] not in tickets):
                return []

        for node in graph[arrive]:
            if ([arrive, node] in visited and [arrive, node] in tickets):
                idx = visited.index([arrive, node])
                if (visited[idx] != 1):
                    visited[idx] = 1
                    dfs(arrive, node, route)
        return []

    total_ans = []
    for i in range(len(tickets)):
        ans = []

        # tickets를 visited에 복사
        visited = []
        for j in range(len(tickets)):
            visited.append(tickets[j])

        # ICN으로 시작하면 해당 티켓부터 사용해서 탐색 시작
        if (tickets[i][0] == "ICN"):
            visited[i] = 1

            ans = dfs(tickets[i][0], tickets[i][1], [])

            # print(ans)

            if (visited.count(1) == len(visited) and ans != 0):
                total_ans.append(ans)
            # print("==")

    # print(total_ans)
    if (total_ans):
        total_ans.sort()
        answer = total_ans[0]

    return answer
"""

## DFS+백트래킹
"""
from collections import defaultdict
import copy

def solution(tickets):
    answer = []

    graph = defaultdict(list)

    for i in range(len(tickets)):
        graph[tickets[i][0]].append(tickets[i][1])
        graph[tickets[i][0]].sort()

    print(graph)

    def dfs(depart, route):
        route.append(depart)

        for i in range(len(graph[depart])):
            if (graph[depart][i] == 0):  # 방문한 곳이라면 건너뛰기
                continue
            else:
                arrive = graph[depart][i]  # 해당 출발지에서 갈 수 있는 도착지
                graph[depart][i] = 0  # 방문 처리

                tmp = dfs(arrive, route)  # 해당 루트로 갈수있는 곳까지 가보기

                if (len(tmp) == len(tickets) + 1):  # 만약 모든 티켓을 사용했다면 -> 일단 result에 추가
                    result.append(copy.deepcopy(tmp))

                # 백트래킹 (되돌려놓기, 다음 루트를 위해)
                route.pop()
                graph[depart][i] = arrive

        return route

    result = []
    dfs("ICN", [])

    result.sort()
    answer = result[0]

    return answer
"""

## DFS 깔끔 풀이
from collections import defaultdict


def solution(tickets):
    answer = []

    # 그래프 생성
    graph = defaultdict(list)

    for i in range(len(tickets)):
        graph[tickets[i][0]].append(tickets[i][1])
        graph[tickets[i][0]].sort()

    # DFS 탐색
    def dfs(tickets, route, N, visited):
        if (len(route) == N + 1):   # 현재 모든 티켓을 사용한만큼의 길이라면 -> return
            return route

        for i in range(N):
            if (visited[i] == 0 and tickets[i][0] == route[-1]):    # i번째 티켓을 사용하지 않았고 and 마지막 도착지가 현재 출발지라서 존재하는 티켓을 사용 가능할 때
                visited[i] = 1      # 티켓 사용 처리
                tmp = dfs(tickets, route + [tickets[i][1]], N, visited)     # 갈 수 있는데까지 탐색
                visited[i] = 0      # 다시 반환
                if (tmp):
                    return tmp

    N = len(tickets)
    visited = [0 for _ in range(N)]

    tickets.sort()
    r = dfs(tickets, ["ICN"], N, visited)

    print(r)
    answer = r

    return answer


if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    # ["ICN", "JFK", "HND", "IAD"]
    # print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
    # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    # print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
    # ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
    # print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))
    # ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]