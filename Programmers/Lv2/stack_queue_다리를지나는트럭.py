def solution(bridge_length, weight, truck_weights):
    answer = 0

    # 다리에는 트럭이 최대 bridge_length대 올라갈 수 있음
    # 다리는 weight 이하까지의 무게를 견딜 수 있음

    bridge = [0 for _ in range(bridge_length)]      # 다리 큐 (다리 길이만큼의 배열을 선언하여 한칸씩 밀리며 트럭이 지나갈 예정)

    ### 정답 코드
    sum_weight = 0      # 다리 위 트럭의 무게 합
    while(len(bridge) > 0):
        sum_weight -= bridge.pop(0)     # 다리 큐가 밀리면서 차가 지나가게 된다면 다리의 무게 합에서 빼주어야 함
        answer += 1

        if(len(truck_weights) > 0):     # 대기 트럭이 남아있지 않을 때까지 반복
            if(truck_weights[0] + sum_weight <= weight):        # 현재 다리 위의 트럭 무게 + 대기 트럭 무게가 다리를 건널 수 있는 무게라면
                sum_weight += truck_weights[0]                  # 다리 위에 해당 트럭이 올라가면 무게 합에 더해줌
                bridge.append(truck_weights.pop(0))             # 다리 위에 올라감
            else:
                bridge.append(0)        # 지나갈 수 없는 무게라면 못 올라가지만 트럭들은 이동해야 하므로 0을 추가하며 밀어줌

    ### 테스트케이스 5번 시간초과
    # while(len(bridge) > 0):
    #     bridge.pop(0)       # 다리 큐 한칸씩 밀기
    #     answer += 1         # 밀게 되면 차가 지나가게 되므로 시간 + 1
    #
    #     if(len(truck_weights) > 0):    # 대기 트럭이 남아있지 않을 때까지 반복
    #         if(truck_weights[0] + sum(bridge) <= weight):      # 현재 다리 위의 트럭 무게 + 대기 트럭 무게가 다리를 건널 수 있는 무게라면
    #             bridge.append(truck_weights.pop(0))            # 다리에 올라감
    #         else:
    #             bridge.append(0)    # 지나갈 수 없는 무게라면 못 올라가지만 트럭은 지나가야 하므로 0을 추가하여 밀어주는 형태 완성

    return answer


if __name__ == '__main__':
    print(solution(2, 10, [7,4,5,6]))
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))


# ### 이전 코드 (테케 실패)
# can_pass = []
#
# for truck in truck_weights:
#     if ((sum(can_pass) + truck) > weight or len(can_pass) + 1 > bridge_length):
#         while(len(can_pass) > 0):
#             can_pass.pop(0)
#             answer += bridge_length
#
#     can_pass.append(truck)
#
# if(len(can_pass) > 0):
#     trucks = 0
#     while (len(can_pass) > 0):
#         can_pass.pop(0)
#         trucks += 1
#     answer += bridge_length + trucks
