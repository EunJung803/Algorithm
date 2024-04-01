import copy

N, K = map(int, input().split())
safty = list(map(int, input().split()))

# 무빙워크 한칸 회전
# 무빙워크 올라간 사람 순서대로 -> 회전하는 방향으로 한칸 이동 가능하면 이동
    # 앞에 사람 있거나 or 안정성이 0이면 이동 X
# 1번 칸에 사람이 없고 and 안정성이 0이 아니면 -> 사람 올리기 1번에
# 안정성이 0개인 칸이 K개 이상 -> 종료
# n번 칸에 사람이 도착하면 -> 바로 내림

## 무빙워크 배열 생성
movingWalk = []         # [초기 인덱스, 해당 인덱스의 안정성]
for i in range(2*N):
    movingWalk.append([i, safty[i]])

## 무빙워크 회전시키는 함수
def rotate_movingWalk(movingWalk):
    last_one = movingWalk[-1]       # 가장 끝에 있는 건 -> 맨 처음으로 이동해야함
    new_movingWalk = [last_one]     # 원래 가장 끝에 있던걸 맨 처음으로 넣어주고 -> for문으로 2N-1까지 순서대로 그 뒤에 넣어주기
    for i in range(2*N-1):
        new_movingWalk.append(movingWalk[i])
    return new_movingWalk

## 무빙워크 위에 서있는 사람도 회전되는 함수
def rotate_ppl(ppl_loc, ppl_seq):
    # 사람이 한명이라도 서있다면 -> 회전
    if(ppl_loc):
        # 무빙워크 회전시킨 것과 동일하게 회전시킴
        last_one = ppl_loc[-1]
        new_ppl_loc = [last_one]
        for i in range(2*N-1):
            if(i == N-2):       # 만약 N번 칸 위에 사람이 위치하게 된다면 -> 내려야하므로 0 넣기
                new_ppl_loc.append(0)
                continue
            else:
                new_ppl_loc.append(ppl_loc[i])

        # 사람 위치 리스트 조정 후 -> 해당 위치에 서있는 사람 인덱스 순서대로 업데이트
        new_ppl_seq = []
        for i in range(len(new_ppl_loc)-1, -1, -1):      # 가장 끝에서부터 서있는 사람이 제일 먼저 들어왔을 것이므로 뒤에서부터 순서대로 넣어줌
            if(new_ppl_loc[i] == 1):
                new_ppl_seq.append(i)
        return new_ppl_loc, new_ppl_seq


ppl_loc = [0 for _ in range(2*N)]      # 사람 위치 리스트 (0 : 사람없음, 1: 사람있음)
ppl_seq = []                           # 올라간 사람들의 순서 (사람 인덱스별로 담음)

## 사람이 한칸 움직이는 함수
def ppl_move():
    global ppl_seq
    if(ppl_seq):
        for i in range(len(ppl_seq)):   # 들어온 순서대로 진행
            curr_idx = ppl_seq[i]                   # 현재 사람 인덱스
            next_idx = (curr_idx + 1) % (2*N)       # 한칸 이동 후의 인덱스
            if(ppl_loc[next_idx] == 0 and movingWalk[next_idx][1] > 0):     # 앞에 한칸 이동할 곳이 이동 가능한 곳이라면
                if (next_idx == N-1):     # 그러나 N의 위치로 이동하게 되면 사람 내림 처리
                    movingWalk[next_idx][1] -= 1
                    ppl_loc[curr_idx] = 0
                    ppl_seq[i] = -1       # 내린 사람은 -1로 우선 처리
                else:
                    movingWalk[next_idx][1] -= 1    # 이동한 칸의 안정성 - 1
                    ppl_loc[next_idx] = 1           # 한칸 이동
                    ppl_loc[curr_idx] = 0
                    ppl_seq[i] = next_idx           # 사람 인덱스 업데이트

        # 내림 처리 된 사람 제외하고 담아서 사람 순서 리스트 업데이트해주기
        new_ppl_seq = []
        for i in range(len(ppl_seq)):
            if(ppl_seq[i] != -1):
                new_ppl_seq.append(ppl_seq[i])
        ppl_seq = copy.deepcopy(new_ppl_seq)

## 안정성이 0인 개수 확인 함수
def count_zero():
    zero_cnt = 0
    for i in range(2*N):
        if(movingWalk[i][1] <= 0):
            zero_cnt += 1
    return zero_cnt

## Main 실행
level= 0    # 실험 횟수
while(True):
    level += 1
    ## 1.
    movingWalk = rotate_movingWalk(movingWalk)          # 무빙워크 1칸 회전
    ppl_loc, ppl_seq = rotate_ppl(ppl_loc, ppl_seq)     # 무빙워크 위 사람도 동일하게 1칸 회전

    ## 2.
    ppl_move()      # 사람 이동

    ## 3.
    if(ppl_loc[0] == 0 and movingWalk[0][1] > 0):       # 1번 칸에 사람 배치
        ppl_loc[0] = 1
        ppl_seq.append(0)
        movingWalk[0][1] -= 1

    ## 4.
    if(count_zero() >= K):      # 안정성이 0인 칸이 K개 이상이면 종료
        print(level)
        break