def solution(board, moves):
    answer = 0

    basket = []     # 뽑은 인형을 담는 바구니
    last_doll = 0   # 바구니에서 쌓인 인형 중 가장 위에 있는 인형을 저장해둘 변수

    for i in moves:
        # 보드의 [row][col] 중 col은 고정으로 moves에서 선택한 값에 의해 결정되고, row를 바꿔가며 탐색해야지 세로로 탐색하게 된다.
        for j in range(len(board)):
            if (board[j][i - 1] != 0):              # 만약 0이 아니라 숫자가 들어있는걸 만난다면 -> 이게 제일 맨 위에 있는 인형이다.
                basket.append(board[j][i - 1])      # 가장 위에 있는 인형이므로 우선 바구니에 넣어준다

                if (basket[-1] == last_doll):       # 만약 같은 인형종류가 들어왔던 것이면 -> 둘 다 터지면서 answer에 2개 추가
                    basket.pop(-1)
                    basket.pop(-1)
                    answer += 2

                if (len(basket) > 0):           # 인형이 터지면서 바구니가 아예 텅 비어버리면 마지막 인형을 저장할 필요가 없음
                    last_doll = basket[-1]      # 그게 아니라면 현재 바구니 상태에서 가장 위에 있는 인형을 저장하기 (다음 루프때 같은게 들어오는지 비교해야 하니까)

                board[j][i - 1] = 0         # 뽑힌 인형의 자리는 0으로 만들어서 이미 뽑혔다는 것을 업데이트!
                break

    print(basket)

    return answer

solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])
solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [0, 2, 4, 4, 2], [0, 5, 1, 3, 1]], [1, 2, 2])      # basket이 중간에 빈 배열이 되는 경우