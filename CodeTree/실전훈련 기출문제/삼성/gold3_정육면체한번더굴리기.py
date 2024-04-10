import copy
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

q = deque()

# 상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= N):
        return False
    return True

# 인접한 같은 숫자로 점수 찾기 (BFS)
def bfs():
    score = 0
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        num = curr[2]

        score += num

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(check_range(nx, ny) and visited[nx][ny] == 0 and board[nx][ny] == num):
                visited[nx][ny] = 1
                q.append((nx, ny, num))
    return score

# 주사위 굴리는 함수
def roll(dice, direct):
    # 위
    if(direct == 0):
        rolled_dice = [(dice[1][0], dice[1][1]), (dice[0][1], dice[0][0]), (dice[2][0], dice[2][1])]
        dice = copy.deepcopy(rolled_dice)
        return dice

    # 오른쪽
    if(direct == 1):
        rolled_dice = [(dice[2][1], dice[2][0]), (dice[1][0], dice[1][1]), (dice[0][0], dice[0][1])]
        dice = copy.deepcopy(rolled_dice)
        return dice

    # 아래
    if(direct == 2):
        rolled_dice = [(dice[1][1], dice[1][0]), (dice[0][0], dice[0][1]), (dice[2][0], dice[2][1])]
        dice = copy.deepcopy(rolled_dice)
        return dice

    # 왼쪽
    if(direct == 3):
        rolled_dice = [(dice[2][0], dice[2][1]), (dice[1][0], dice[1][1]), (dice[0][1], dice[0][0])]
        dice = copy.deepcopy(rolled_dice)
        return dice


## Main 실행 ##

my_dice = [(1, 6), (2, 5), (3, 4)]      # 주사위

total = 0               # 점수 합
my_direction = 1        # 내 주사위가 바라보는 방향 (처음은 무조건 오른쪽)
my_loc = [0, 0]         # 내 주사위 위치

for _ in range(M):
    visited = [list(0 for _ in range(N)) for _ in range(N)]     # 초기화

    # 1. 방향대로 주사위 굴리기
    my_dice = roll(my_dice, my_direction)

    # 1-1. 주사위 위치 업데이트
    my_loc[0] += dx[my_direction]
    my_loc[1] += dy[my_direction]

    dice_num = my_dice[0][1]                    # 바닥면 주사위 숫자
    board_num = board[my_loc[0]][my_loc[1]]     # 주사위가 놓여있는 위치의 보드값

    # 2. 현재 주사위 위치에서 BFS로 점수 구하기
    q.append((my_loc[0], my_loc[1], board_num))
    visited[my_loc[0]][my_loc[1]] = 1
    total += bfs()

    # 3. 다음 방향 결정하기
    if(board_num < dice_num):     # 시계방향 90도
        my_direction = (my_direction + 1) % 4

    if(board_num > dice_num):     # 반시계방향 90도
        my_direction = (my_direction - 1) % 4

    if(board_num == dice_num):
        pass

    # 3-1. 현재 방향에서 이동한다고 가정했을 때, 격자 범위를 벗어나는지 확인해보기
    tmp_x = my_loc[0] + dx[my_direction]
    tmp_y = my_loc[1] + dy[my_direction]
    if(check_range(tmp_x, tmp_y) == False):     # 범위 밖이면 반대 방향으로 꺾어주기
        my_direction = (my_direction + 2) % 4

print(total)