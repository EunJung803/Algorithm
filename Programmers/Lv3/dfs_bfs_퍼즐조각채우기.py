from collections import deque


def solution(game_board, table):
    answer = 0

    N = len(game_board)

    def check_range(x, y):
        if (x < 0 or y < 0 or x >= N or y >= N):
            return False
        return True

    """
    조각은 한 번에 하나씩 채워 넣습니다.
    조각을 회전시킬 수 있습니다.
    조각을 뒤집을 수는 없습니다.
    게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안 됩니다. (== 퍼즐 조각을 넣었을 때, 빈 공간이 있으면 안됨)
    """

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = [list(0 for _ in range(N)) for _ in range(N)]
    q = deque()

    ### 블럭의 인덱스들을 모아서 구함 (BFS)
    def get_block(q):
        block = []
        while (q):
            curr = q.popleft()
            x, y = curr[0], curr[1]
            block.append((x, y))

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (check_range(nx, ny) and visited[nx][ny] == 0 and table[nx][ny] == 1):
                    q.append([nx, ny])
                    visited[nx][ny] = 1

        return block

    ### 모든 블럭들의 좌표를 get_block 함수를 이용해서 total_blocks 리스트에 담기
    total_blocks = []
    for i in range(N):
        for j in range(N):
            if (table[i][j] == 1 and visited[i][j] == 0):
                q.append([i, j])
                visited[i][j] = 1
                b = get_block(q)
                total_blocks.append(b)

    # print(total_blocks)

    ### 빈칸의 인덱스들을 모아서 구함 (BFS)
    def get_blank(q):
        blank = []
        while (q):
            curr = q.popleft()
            x, y = curr[0], curr[1]
            blank.append((x, y))

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (check_range(nx, ny) and visited[nx][ny] == 0 and game_board[nx][ny] == 0):
                    q.append([nx, ny])
                    visited[nx][ny] = 1

        return blank

        ### 모든 빈칸들의 좌표를 get_blank 함수를 이용해서 total_blanks 리스트에 담기

    visited = [list(0 for _ in range(N)) for _ in range(N)]
    total_blanks = []

    for i in range(N):
        for j in range(N):
            if (game_board[i][j] == 0 and visited[i][j] == 0):
                q.append([i, j])
                visited[i][j] = 1
                b = get_blank(q)
                total_blanks.append(b)

    # print(total_blanks)

    ### 들어오는 도형의 좌표들을 90도 회전하여 리턴하는 함수
    def rotate(arr):
        rotate_arr = []
        n = len(arr)
        for a in range(len(arr)):
            x = arr[a][0]
            y = arr[a][1]

            # 시계방향 90도 회전하기
            new_x = y
            new_y = (n - 1) - x

            rotate_arr.append((new_x, new_y))

        return rotate_arr

    ### 블럭 채워보기
    inserted = [0 for _ in range(len(total_blanks))]
    used = [0 for _ in range(len(total_blocks))]

    for i in range(len(total_blocks)):
        selected = total_blocks[i]  # 블럭 선택

        for j in range(len(total_blanks)):

            # 빈칸에 빠짐없이 들어갈 수 있고 + 비어있는 빈칸이고 + 사용하지 않았던 블럭이면
            if (len(selected) == len(total_blanks[j]) and inserted[j] == 0 and used[i] == 0):
                q.append([selected, total_blanks[j]])
                # print(q)

            can_fit = []
            erase_blank = []
            while (q):
                curr = q.popleft()
                curr_block = curr[0]
                curr_blank = curr[1]

                curr_block.sort()
                curr_blank.sort()

                idx_set = set()
                for b in range(len(curr_block)):
                    # 각 인덱스의 차이를 set에 담기
                    idx_set.add((curr_block[b][0] - curr_blank[b][0], curr_block[b][1] - curr_blank[b][1]))

                # 모든 차이가 동일하면 -> 해당 빈칸에 들어갈 수 있음
                if (len(idx_set) == 1):
                    can_fit.append(curr_block)
                    erase_blank.append(curr_blank)

                # 동일하지 않으면 -> 회전 시켜보기
                if (len(idx_set) != 1):
                    for _ in range(4):
                        idx_set = set()
                        curr_block = rotate(curr_block)  # 회전시켜서 시도

                        curr_block.sort()

                        for b in range(len(curr_block)):
                            idx_set.add((curr_block[b][0] - curr_blank[b][0], curr_block[b][1] - curr_blank[b][1]))

                        if (len(idx_set) == 1):  # 회전시키면 끼워맞출 수 있을 때
                            can_fit.append(curr_block)
                            erase_blank.append(curr_blank)
                            break

            if (can_fit and erase_blank):
                inserted[j] = 1
                used[i] = 1

            for f in range(len(can_fit)):
                answer += len(can_fit[f])

    return answer