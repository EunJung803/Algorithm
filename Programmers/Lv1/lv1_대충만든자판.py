def solution(keymap, targets):
    answer = []

    # keymap[i] == i+1번키
    # i+1번키 를 3번 누르면 i번째 인덱스의 문자열에서 2번째 요소를 가르킴

    for t in targets:
        press = 0   # answer에 넣게 되는 최종적인 최소 횟수
        keymap_press_num = [0 for _ in range(len(keymap))]      # 각 n번 키마다 target에 대해서 자판을 누를 수 있는 횟수를 저장할 배열
                                                                # (ex. keymap_press_num = [1, 2] -> 이러면 1번키는 1번, 2번키는 2번 눌러야 해당 target의 원소)
        for i in range(len(t)):             # t = "ABCD", t[0] = "A"
            for j in range(len(keymap)):    # keymap[j] = "ABACD"
                if(keymap[j].find(t[i]) != -1):                         # 만약 target의 요소가 keymap 안에 존재한다면
                    keymap_press_num[j] = keymap[j].find(t[i]) + 1      # 인덱스 + 1 해서 해당 인덱스번 키에 그만큼 누를 수 있다고 저장
                else:
                    keymap_press_num[j] = 999       # 존재하지 않다면 그냥 큰 수 저장

            if(min(keymap_press_num) == 999):       # 최솟값이 그러나 999라면, 누를 수 없는 상태 == 이 키맵으로는 목표 문자열 만들기 실패 -> -1을 저장하고 다음 타겟 살펴보기 위해 break
                press = -1
                break
            else:
                press += min(keymap_press_num)      # 최솟값이 999가 아니면 -> 누를 수 있다 ! == 이 키맵으로 목표 문자열 만들 수 있음, 최소 횟수를 구하기 위해 min 사용 -> 저장

        answer.append(press)

    return answer

if __name__ == '__main__':
    print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
    print(solution(["AA"], ["B"]))
    print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))
    print(solution(["BC"], ["AC", "BC"]))       # 중간에 break 도입 전 반례, 정답 : [-1, 3]