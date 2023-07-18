def solution(cards1, cards2, goal):
    answer = ''

    # 1-0 / 2-0 / 2-1 / 1-1 / 1-2 -> O
    # 1-0 / 2-0 / 2-1 / 1-2 / 1-1 -> X

    i_one = 0
    i_two = 0

    for i in range(len(goal)):
        check = False

        if(goal[i] == cards1[i_one]):
            i_one += 1
            if (i_one == len(cards1)):
                i_one -= 1
            check = True
        elif(goal[i] == cards2[i_two]):
            i_two += 1
            if(i_two == len(cards2)):
                i_two -= 1
            check = True

        if(check == False):
            answer += "No"
            break


    if (len(answer) == 0):
        answer += "Yes"

    return answer


if __name__ == '__main__':
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
    print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))