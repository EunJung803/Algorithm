from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

t = int(input())

def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def bfs(q):
    q.append(home)
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        if(get_dist(x, y, fest[0], fest[1]) <= 1000):
            print("happy")
            return

        for i in range(n):
            if(visited[i] == 0):
                dist = get_dist(x, y, conv[i][0], conv[i][1])
                if(dist <= 1000):
                    q.append(conv[i])
                    visited[i] = 1
    print("sad")
    return

for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    conv = [list(map(int, input().split())) for _ in range(n)]
    fest = list(map(int, input().split()))

    q = deque()

    visited = [0 for i in range(n+1)]
    bfs(q)