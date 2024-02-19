# 1 : [0~i][j]
# 2 : 상하좌우
# 3 : 대각선

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

bomb_m = [[0 for _ in range(n)] for _ in range(n)]

d1 = [(-2, 0), (-1, 0), (1, 0), (2, 0)]    # 1번 폭탄의 피해 방향
d2 = [(-1, 0), (1, 0), (0, 1), (0, -1)]    # 2번 폭탄의 피해 방향
d3 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # 3번 폭탄의 피해 방향

bomb_index = []

arr = []
ans = []

## bomb_m 초기화 함수
def init_bomb_m():
    bomb_m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(bomb_index)):
        bomb_m[bomb_index[i][0]][bomb_index[i][1]] = 1
    return bomb_m

## 폭탄의 피해범위 구하기
def bomb_explosion(arr):
    # 변수 초기화
    bomb_m = init_bomb_m()
    count = len(arr)

    # 폭탄 종류에 맞춰서 각 폭탄이 존재하는 인덱스에 해당 폭탄 종류가 터졌을 때의 맵 상황 bomb_m에 기록하기 (0은 빈킨, 1은 피해입은칸)
    for b in range(len(arr)):
        bx = bomb_index[b][0]
        by = bomb_index[b][1]

        if (arr[b] == 1):       # 1번 폭탄
            for j in range(len(d1)):
                dx = d1[j][0]
                dy = d1[j][1]
                if (bx + dx < n and by + dy < n and bx + dx >= 0 and by + dy >= 0):
                    if (bomb_m[bx + dx][by + dy] == 0):
                        bomb_m[bx + dx][by + dy] = 1
                        count += 1

        if (arr[b] == 2):       # 2번 폭탄
            for j in range(len(d2)):
                dx = d2[j][0]
                dy = d2[j][1]
                if (bx + dx < n and by + dy < n and bx + dx >= 0 and by + dy >= 0):
                    if (bomb_m[bx + dx][by + dy] == 0):
                        bomb_m[bx + dx][by + dy] = 1
                        count += 1

        if (arr[b] == 3):       # 3번 폭탄
            for j in range(len(d3)):
                dx = d3[j][0]
                dy = d3[j][1]
                if (bx + dx < n and by + dy < n and bx + dx >= 0 and by + dy >= 0):
                    if (bomb_m[bx + dx][by + dy] == 0):
                        bomb_m[bx + dx][by + dy] = 1
                        count += 1

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

# print(ans)
print(max(ans))