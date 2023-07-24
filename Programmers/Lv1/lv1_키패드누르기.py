def solution(numbers, hand):
    answer = ''

    # 왼 엄지 -> 1 4 7
    # 오른 엄지 -> 3 6 9
    # 둘 중 더 가까운 엄지, 같다면 자신 손잡이 엄지 -> 2 5 8 0

    keypad = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]       # keypad[0] : 왼손이 누르는 키패드 / keypad[1] : 거리를 비교해야하는 키패드 / keypad[2] : 오른손이 누르는 키패드
    left_hand = []      # 왼손의 위치를 저장할 배열
    right_hand = []     # 오른손의 위치를 저장할 배열

    for num in numbers:
        for j in range(len(keypad)):        # numbers의 숫자가 keypad의 어느 인덱스에 있는지 찾기
            if (num in keypad[j]):
                if (j == 0):        # 왼손이 누르는 키패드
                    left_hand.append(num)
                    answer += "L"
                if (j == 2):        # 오른손이 누르는 키패드
                    right_hand.append(num)
                    answer += "R"
                if (j == 1):        # 거리를 비교해서 -> 다르면 거리가 더 짧은 손으로 누르기, 같으면 hand에 나와있는 손으로 누르기
                    # 거리 비교
                    for x in range(len(keypad)):
                        if(len(left_hand) == 0):            # 왼손 위치 배열이 비어있으면, 아직 왼손은 * 위치에 있음
                            left_current_index = (0, 3)
                        else:                               # 비어있지 않다면, 현재 왼손이 위치한 숫자의 좌표 구하기 (x, y)
                            if(left_hand[-1] in keypad[x]):
                                left_current_index = (x, keypad[x].index(left_hand[-1]))
                        if (len(right_hand) == 0):          # 오른손 위치 배열이 비어있다면, 아직 오른손은 # 위치에 있음
                            right_current_index = (2, 3)
                        else:                               # 비어있지 않다면, 현재 오른손이 위치한 숫자의 좌표 구하기 (x, y)
                            if(right_hand[-1] in keypad[x]):
                                right_current_index = (x, keypad[x].index(right_hand[-1]))

                    keypad_index = (1, keypad[1].index(num))    # 현재 눌러야 할 키패드의 좌표 위치 (x, y)

                    left_distance = abs(left_current_index[0] - keypad_index[0]) + abs(left_current_index[1] - keypad_index[1])     # 왼손과 키패드의 거리
                    right_distance = abs(right_current_index[0] - keypad_index[0]) + abs(right_current_index[1] - keypad_index[1])  # 오른손과 키패드의 거리

                    if(left_distance < right_distance):     # 왼손 거리가 더 짧으면 왼손으로 누르기
                        left_hand.append(num)
                        answer += "L"
                    if (left_distance > right_distance):    # 오른손 거리가 더 짧으면 오른손으로 누르기
                        right_hand.append(num)
                        answer += "R"
                    if (left_distance == right_distance):   # 거리가 같다면, hand에 나와있는대로 누르기
                        if(hand == "left"):
                            left_hand.append(num)
                            answer += "L"
                        if(hand == "right"):
                            right_hand.append(num)
                            answer += "R"

    # print(left_hand)
    # print(right_hand)

    return answer

if __name__ == '__main__':
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))     # "LRLLLRLLRRL"
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))      # "LRLLRRLLLRR"
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))        # "LLRLLRLLRL"
