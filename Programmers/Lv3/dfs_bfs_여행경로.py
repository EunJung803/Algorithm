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

if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    # ["ICN", "JFK", "HND", "IAD"]
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
    # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
