def solution(key, lock):
    answer = False

    m = len(key)
    n = len(lock)

    # 보드 확장
    board = [list(0 for _ in range((m * 2) + n)) for _ in range((m * 2) + n)]

    for i in range(n):
        for j in range(n):
            if (lock[i][j] == 1):
                board[m + i][m + j] = 1
            if (lock[i][j] == 0):
                board[m + i][m + j] = 0

    #     for i in range(len(board)):
    #         print(board[i])
    #     print("==")

    # 회전한 배열 반환
    def rotate(arr):
        l = len(arr)
        rotated = [list(0 for _ in range(l)) for _ in range(l)]
        for i in range(len(arr)):
            for j in range(len(arr)):
                rotated[j][l - 1 - i] = arr[i][j]
        return rotated

    # 보드에서 lock의 위치에 모두 1로 다 맞았는지
    def check_open(board):
        for i in range(n):
            for j in range(n):
                if (board[m + i][m + j] != 1):
                    return False
        return True

    # 키를 90도씩 회전하며 -> 보드 전체 탐색 -> 맞는 부분이 있다면 True
    for r in range(4):
        key = rotate(key)

        for i in range(m + n + 1):
            for j in range(m + n + 1):

                # key 보드에 끼우기
                tmp = 0
                for a in range(m):
                    for b in range(m):
                        board[i + a][j + b] += key[a][b]
                        tmp += board[i + a][j + b]

                # print(tmp, i, j)
                # for _ in range(len(board)):
                #     print(board[_])
                # print("////")

                # lock에 맞는지 검사
                if (check_open(board)):
                    return True

                # 안맞으면 보드 다시 원래대로
                for a in range(m):
                    for b in range(m):
                        board[i + a][j + b] -= key[a][b]

    return answer

## 이전 코드
# 이전 코드 실패 이유 : "이동 → 회전" 을 반복하여 자물쇠를 열 수 있는 상태인지 확인하려함
# 그러나 "회전 → 이동" 의 예외가 존재 + 이동이 너무 고정적이라 모든 경우를 체크하지 X
# 회전을 먼저 하고 이동을 모든 위치에 시켜봤어야 했다
"""
def solution(key, lock):
    answer = False
    
    m = len(key)
    n = len(lock)
    
    # 끼우는 놈의 인덱스 (돌기 부분 담기)
    key_idx = []
    for i in range(m):
        for j in range(m):
            if(key[i][j] == 1):
                key_idx.append((i, j))
    
    # 끼워 맞춰야하는 부분의 인덱스 (홈 부분 담기)
    lock_idx = []
    for i in range(n):
        for j in range(n):
            if(lock[i][j] == 0):
                lock_idx.append((i, j))
    
    # print(key_idx)
    # print(lock_idx)
    
    # 범위 확인 (열쇠만 이동하니까 열쇠 기준)
    def check_range(x, y):
        if(x < 0 or y < 0 or x >= n or y >= n):
            return False
        return True
    
    # 회전    
    def rotate(arr):
        l = len(arr)
        rotated = []
        for i in range(len(arr)):
            x, y = arr[i][0], arr[i][1]
            nx, ny = y, (l-1)-x
            rotated.append((nx, ny))
        return rotated
    
    # 이동 == 밀어버리기
    def move(arr, direction, move_block):
        new_arr = []
        if(direction == 0):     # 상
            for i in range(len(arr)):
                nx = arr[i][0]-move_block
                ny = arr[i][1]
                if(check_range(nx, ny)):
                    new_arr.append((nx, ny))
                else:
                    continue
        if(direction == 1):     # 하
            for i in range(len(arr)):
                nx = arr[i][0]+move_block
                ny = arr[i][1]
                if(check_range(nx, ny)):
                    new_arr.append((nx, ny))
                else:
                    continue
        if(direction == 2):     # 좌
            for i in range(len(arr)):
                nx = arr[i][0]
                ny = arr[i][1]-move_block
                if(check_range(nx, ny)):
                    new_arr.append((nx, ny))
                else:
                    continue
        if(direction == 3):     # 우
            for i in range(len(arr)):
                nx = arr[i][0]
                ny = arr[i][1]+move_block
                if(check_range(nx, ny)):
                    new_arr.append((nx, ny))
                else:
                    continue
        return new_arr
    
    # 자물쇠가 현재 열쇠로 열리는지 확인
    def check_open(arr1, arr2):
        if(len(arr1) != len(arr2)):
            return False
        else:
            idx = set()
            sort_arr1 = sorted(arr1)
            sort_arr2 = sorted(arr2)
            for i in range(len(arr1)):
                idx.add((sort_arr1[i][0] - sort_arr2[i][0], sort_arr1[i][1] - sort_arr2[i][1]))
            if(len(idx) != 1):
                return False
        return True
    
    # 1. 현재 키의 모양으로 열 수 있는지 ?
        # 아니라면 회전 4방향 다 해보고 -> 열리면 True
    # 1-1. 동일한 크기가 아니면 -> 이동시켜보기 (4방향 다)
        # 1-1-1. 이동했을 때 홈이 구멍의 크기와 같다면 -> 이동 시킨 후의 모양으로 열수있으면 True, 아니라면 회전
    # 1-2. 동일한 크기라면 -> 들어맞는지 검사
        # 1-2-1. 안들어맞으면 -> 회전 (90도씩)
    
    # 자물쇠의 홈과 키의 돌기가 하나도 존재하지 않을 때
    if(len(key_idx) == 0 and len(lock_idx) == 0):
        return False
    
    # 자물쇠가 무슨 키로든 열릴 때 (모든 부분이 홈이라서)
    if(len(lock_idx) == 0):
        return True
    
    # 현재 키 모양 그대로 자물쇠가 열릴 때
    if(check_open(key_idx, lock_idx) == True):
        return True
    
    # 그렇지 않은 경우,
    if(check_open(key_idx, lock_idx) == False):
        # 1) 이동 전에 우선 키 모양 회전해보기
        if(len(key_idx) == len(lock_idx)):
            for i in range(4):
                rotated_key = rotate(key_idx)
                if(check_open(rotated_key, lock_idx)):
                    return True
                
        # 2) 회전으로도 안되면 이동해서 키의 크기가 달라져야함
        cnt = 1
        while(cnt <= n*2):
            # print("==")
            # 일단 상하좌우 한칸씩 이동시켜보기
            for i in range(4):
                moved_key = move(key_idx, i, cnt)
                
                # print(moved_key, " / ", key_idx)
                
                if(len(moved_key) == 0):
                    continue 
                
                # 1. 이동 했는데 홈과 구멍의 크기가 같을때
                if(len(moved_key) == len(lock_idx)):        # 이동 시켰을 때 이 모양으로 열 수 있으면 True
                    if(check_open(moved_key, lock_idx)):
                        return True
                    else:                                   # 홈과 구멍의 크기는 같은데 모양이 다르다면 -> 회전해보기
                        for j in range(4):
                            moved_key = rotate(moved_key)
                            if(check_open(moved_key, lock_idx)):    # 회전했을 때 열 수 있는 모양이 나오면 True
                                return True
                            
                # 2. 이동 했는데 홈과 구멍의 크기가 다를때 
                else:
                    continue

            # 1칸 이동 + 회전해도 열 수 없음 -> 더 이동하기 위해 cnt++
            cnt += 1
            
        return False
                
    return answer
"""