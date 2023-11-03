# 1 : [0~i][j]
# 2 : 상하좌우
# 3 : 대각선

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# n = 4
# matrix = [[0, 0, 0, 0],
#           [0, 0, 1, 0],
#           [0, 1, 0, 0],
#           [0, 0, 0, 0]]

bomb_m = [[0 for _ in range(n)] for _ in range(n)]

# 폭탄의 피해 방향
d_list = [[(-2, 0), (-1, 0), (1, 0), (2, 0)],
          [(-1, 0), (1, 0), (0, 1), (0, -1)],
          [(-1, -1), (-1, 1), (1, -1), (1, 1)]]

bomb_index = []

arr = []
ans = []

## bomb_m 초기화 함수
def init_bomb_m():
    bomb_m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(bomb_index)):
        bomb_m[bomb_index[i][0]][bomb_index[i][1]] = 1
    return bomb_m


## 폭탄의 피해 규모 계산
def cal_explosion(b_num, bx, by):
    bomb_m = init_bomb_m()
    cnt = 0
    idx = b_num - 1
    for j in range(4):
        dx = d_list[idx][j][0]
        dy = d_list[idx][j][1]
        if (bx + dx < n and by + dy < n and bx + dx >= 0 and by + dy >= 0):
            if (bomb_m[bx + dx][by + dy] == 0):
                bomb_m[bx + dx][by + dy] = 1
                cnt += 1
    return cnt


## 폭탄의 피해범위 구하기
def bomb_explosion(arr):
    # 변수 초기화
    count = len(arr)

    # 폭탄 종류에 맞춰서 각 폭탄이 존재하는 인덱스에 해당 폭탄 종류가 터졌을 때의 맵 상황 bomb_m에 기록하기 (0은 빈칸, 1은 피해입은칸)
    for b in range(len(arr)):
        bx = bomb_index[b][0]
        by = bomb_index[b][1]

        count += cal_explosion(arr[b], bx, by)      # 폭탄의 피해규모 계산한거 더해주기

    ans.append(count)


## 폭탄의 종류를 결정해서 조합을 만듦
def get_bomb_list(num):
    if (num == count_b):
        bomb_explosion(arr)  # 만들어진 폭탄의 피해 규모 확인
        return

    for i in range(1, 4):  # 폭탄은 1,2,3 세 종류
        arr.append(i)
        get_bomb_list(num + 1)
        arr.pop()
    return


### main 실행 부분
count_b = 0
for i in range(n):
    for j in range(n):
        if (matrix[i][j] == 1):
            count_b += 1  # 폭탄의 개수 카운트
            bomb_index.append((i, j))  # 폭탄의 인덱스 저장
            bomb_m[i][j] = 1

get_bomb_list(0)

print(ans)
print(max(ans))