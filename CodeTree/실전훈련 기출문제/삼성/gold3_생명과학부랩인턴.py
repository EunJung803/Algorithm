N, M, K = map(int, input().split())
mold = [list(map(int, input().split())) for _ in range(K)]      # (x, y) / s / d / b

# 상 하 우 좌
dx = [-1,1,0,0]
dy = [0,0,1,-1]

mold_position = [[] for _ in range(K)]
matrix = [[list() for _ in range(M)] for _ in range(N)]

get_mold = 0

## 인덱스 조정 (1씩 빼줌)
for i in range(K):
    mold[i][0] -= 1
    mold[i][1] -= 1
    mold[i][3] -= 1

    mold_position[i] = [mold[i][0], mold[i][1]]     # 현재 위치 저장

## 범위 확인
def check_range(x, y):
    if(x < 0 or y < 0 or x >= N or y >= M):
        return False
    return True

## 곰팡이 이동
def mold_move():
    # global to_eat
    for i in range(K):
        if(mold[i]):
            x = mold[i][0]
            y = mold[i][1]
            s = mold[i][2]
            d = mold[i][3]
            b = mold[i][4]

            nx = x
            ny = y

            for j in range(s):
                nx += dx[d]
                ny += dy[d]
                if(check_range(nx, ny) == False):
                    nx -= dx[d]
                    ny -= dy[d]
                    if(d % 2 == 0):
                        d = (d + 1) % 4
                    else:
                        d = (d - 1) % 4
                    nx += dx[d]
                    ny += dy[d]

            mold[i] = [nx, ny, s, d, b]

            mold_position[i] = [nx, ny]
            matrix[nx][ny].append((b, i))

            ## 이전코드 (시간초과)
            # # 다른 곰팡이가 이미 있어서 만난다면
            # if([nx, ny] in mold_position):
            #     other_mold = mold_position.index([nx, ny])
            #     if(other_mold != i):    # 다른 곰팡이 만나면 -> 둘 중 하나 먹음
            #         mold_position[i] = [nx, ny]
            #         eat_mold(i, other_mold)
            #
            # else:
            #     mold_position[i] = [nx, ny]

## 가장 크기가 큰 곰팡이 빼고 다 먹힘
def eat_mold():
    for i in range(N):
        for j in range(M):
            if(len(matrix[i][j]) > 1):      # 같은 위치에 곰팡이가 2개 이상이라면
                matrix[i][j].sort(key=lambda x:x[0], reverse=True)      # 크기가 가장 큰 순서대로 정렬
                select = matrix[i][j]
                # 뒤에서부터 하나씩 삭제
                while(len(select) > 1):
                    p = matrix[i][j].pop(-1)    # 먹히는 곰팡이
                    # 기존 곰팡이 리스트와 곰팡이 위치 리스트에도 삭제 처리
                    mold[p[1]] = []
                    mold_position[p[1]] = []


## 이전 코드 (시간초과)
# def eat_mold():
#     # 같은 위치에 있는 곰팡이 모두 구해두기
#     get_same_pos = [[] for _ in range(K)]
#     for i in range(K):
#         tmp = [i]
#         if(mold_position[i]):
#             for j in range(i+1, K):
#                 if(mold_position[i] == mold_position[j]):
#                     tmp.append(j)
#             if(len(tmp) > 1):
#                 get_same_pos[i] = tmp
#
#     # print(get_same_pos)
#
#     # 크기가 제일 큰 곰팡이가 나머지 곰팡이 다 먹어버리기
#     for i in range(K):
#         if(get_same_pos[i]):
#             max_mold = 0
#             for j in range(len(get_same_pos[i])):
#                 idx = get_same_pos[i][j]
#                 if(mold[idx] and max_mold < mold[idx][4]):
#                     max_mold = mold[idx][4]
#             for j in range(len(get_same_pos[i])):
#                 idx = get_same_pos[i][j]
#                 if(mold[idx] and max_mold > mold[idx][4]):
#                     mold[idx] = []
#                     mold_position[idx] = []


### Main ###
for c in range(M):
    # 초기화
    flag = True
    matrix = [[list() for _ in range(M)] for _ in range(N)]

    for r in range(N):
        # 채집할 곰팡이를 만난다면
        if(flag and [r, c] in mold_position):
            mold_num = mold_position.index([r, c])
            get_mold += mold[mold_num][4]       # 채집
            # 삭제 처리
            mold[mold_num] = []
            mold_position[mold_num] = []
            flag = False        # 다음 채집은 하지 않기 위해 flag 체크

    # 곰팡이 이동
    mold_move()
    # 이동 후 먹힘 처리
    eat_mold()


print(get_mold)