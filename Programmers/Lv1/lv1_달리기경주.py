def solution(players, callings):

    players_dict = dict()       # 사전 선언

    # 사전에 players 배열 값 세팅하기 (key : 선수이름, value : 인덱스)
    for i, player in enumerate(players):
        players_dict[player] = i

    # 시간 초과 난 이전 코드
    # for i in range(len(callings)):
    #     overtake_index = players.index(callings[i])
    #     passed_index = players.index(callings[i]) - 1
    #
    #     overtake = players[overtake_index]
    #     players[overtake_index] = players[passed_index]
    #     players[passed_index] = overtake

    for i in callings:
        overtake_index = players_dict.get(i)    # 사전으로 추월하는 선수의 인덱스 탐색하기

        players_dict[players[overtake_index]] -= 1          # 추월하는 선수 인덱스 값 바꿔주기 (추월 했으니까 -1)
        players_dict[players[overtake_index - 1]] += 1      # 추월 당하는 선수 인덱스 값 바꿔주기 (추월 당했으니까 +1)

        players[overtake_index], players[overtake_index - 1] = players[overtake_index - 1], players[overtake_index]     # players 배열에서 순서 바꿔주기

    return players

if __name__ == '__main__':
    print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))