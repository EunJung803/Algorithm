def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        can_learn = True
        skill_order = []    # 스킬트리 속 스킬의 순서를 저장할 배열

        for s in skill:
            if(tree.find(s) == -1):     # 대소 비교의 편의를 위해 99로 대입
                skill_order.append(99)
            else:
                skill_order.append(tree.find(s))    # 스킬트리 내의 해당 스킬 인덱스 값 넣기

        # 스킬의 순서 비교하기
        for i in range(0, len(skill_order)-1):
            if(skill_order[i] > skill_order[i+1]):  # 만약 스킬 순서가 틀린게 있다면 -> 해당 스킬트리는 불가능
                can_learn = False
                break

        if(can_learn):      # 모든 순서가 올바른 형태라면 -> 해당 스킬트리는 가능
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
    print(solution("CBD", ["CAD"]))             # 0
    print(solution("CBD", ["AEF", "ZJW"]))      # 2
    print(solution("REA", ["REA", "POA"]))      # 1
    print(solution("CBDK", ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]))      # 4
    print(solution("BDC", ["AAAABACA"]))        # 0
    print(solution("CBD", ["C", "D", "CB", "BDA"]))     # 2