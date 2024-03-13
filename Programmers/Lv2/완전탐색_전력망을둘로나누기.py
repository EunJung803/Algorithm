from collections import deque

def bfs(start_point, graph, visited, connected):
    q = deque()
    q.append(start_point)
    visited[start_point] = 1
    cnt = 1

    while (q):
        curr = q.popleft()

        for i in range(len(graph[curr])):
            next_point = graph[curr][i]
            if(visited[next_point] == 0 and connected[curr][next_point] == 0):      # 이전에 탐색하지 않았고 현재 노드와 연결되어 있다면 -> 카운트
                visited[next_point] = 1
                q.append(next_point)
                cnt += 1
    return cnt


def solution(n, wires):
    answer = n

    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    # print(graph)

    # 끊고 -> 탐색 -> 카운트
    connected = [list(0 for _ in range(n + 1)) for _ in range(n + 1)]  # 0 이면 연결되어있고 1이면 끊겨있기

    for i in range(len(wires)):
        visited = [0 for _ in range(n + 1)]
        left = wires[i][0]
        right = wires[i][1]

        connected[left][right] = 1  # 현재 wires[i] 인 부분을 끊어보기
        connected[right][left] = 1

        left_count = bfs(left, graph, visited, connected)  # left에 붙어있는 전력망 개수
        right_count = bfs(right, graph, visited, connected)  # right에 붙어있는 전력망 개수

        connected[left][right] = 0  # 다음 탐색을 위해 다시 붙여두기
        connected[right][left] = 0

        # print(left_count)
        # print(right_count)
        # print("==")

        answer = min(answer, abs(left_count - right_count))

    return answer


if __name__ == '__main__':
    print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))