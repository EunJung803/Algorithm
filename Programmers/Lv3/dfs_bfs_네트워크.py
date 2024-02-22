from collections import deque

def solution(n, computers):
    answer = 0

    check = [False for _ in range(n)]

    ans = []
    network = []

    q = deque()

    for c in range(n):
        if(check[c] == False):      # 확인하지 않은 컴퓨터 번호라면 큐에 삽입
            q.append(c)

            while(q):
                curr_comp = q.popleft()
                for i in range(n):      # 현재 행의 모든 열을 살펴보면서
                    if(computers[curr_comp][i] == 1 and check[i] == False):     # 만약 연결이 되어있고, 이전에 확인한 기록이 없다면
                        check[i] = True     # 확인했다고 표시
                        network.append(i)   # 하나의 네트워크로 판단하여 network 배열에 삽입
                        q.append(i)         # 연결되어 있는 열에서 또 연결된게 있는지 다음 탐색을 위해 큐에 삽입
        if(network):    # 형성된 네트워크가 있다면 -> ans 배열에 삽입
            ans.append(network)
            network = []

    print(ans)
    answer = len(ans)   # 네트워크의 총 개수는 ans 배열에 들어있는 네트워크들의 개수

    return answer

if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))       # 2
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))       # 1
