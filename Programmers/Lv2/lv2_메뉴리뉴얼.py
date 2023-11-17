from itertools import combinations


def solution(orders, course):
    answer = []

    # 가장 많이 주문한 단품을 -> 코스요리로 구성
    # 코스요리 : 최소 2개 이상의 단품
    # 최소 2명 이상의 손님으로부터 주문된 단품이 코스요리 후보

    ### 가장 많이 주문된 단품메뉴 조합 구하기 (pick_num 개수 만큼 뽑은 조합)
    def get_course(pick_num):
        max_list = set()    # 가장 많이 주문된 단품메뉴 조합을 담을 set()

        # 각 손님이 주문한 메뉴를 기반으로 pick_num만큼 뽑아서 만들 수 있는 조합 모두 check_list에 담기
        check_list = list()
        for i in range(len(orders)):
            arr = list(combinations(orders[i], pick_num))
            for j in range(len(arr)):
                check_list.append(arr[j])

        # orders를 순회하며 check_list에 들어있는 각 조합의 개수가 몇번 주문되었는지를 카운트해서 담을 배열
        find_course = [0 for _ in range(len(check_list))]

        for i in range(len(check_list)):            # ('F', 'G')
            for n in range(len(orders)):            # 'ABCFG'
                flag = True
                for j in range(len(check_list[i])):  # 'F'
                    if (check_list[i][j] not in orders[n]):     # 해당 조합의 요소가 들어있지 않는 주문이라면 flag = False
                        flag = False
                        break
                if (flag):
                    find_course[i] += 1

        if (find_course):   # find_course가 비어있지 않으면 max값 구해서 최대로 주문된 개수의 조합을 max_list에 담기
            get_max = max(find_course)

            if (get_max >= 2):
                for i in range(len(find_course)):
                    if (find_course[i] == get_max):
                        max_list.add(tuple(sorted(check_list[i])))

        return max_list

    ### 정답 구하는 부분
    for i in range(len(course)):
        pick_num = course[i]    # 코스요리를 구성하는 단품메뉴의 개수

        c = get_course(pick_num)    # 해당 개수의 단품메뉴 조합 중 가장 많이 주문된 조합의 set()
        c = list(c)     # set()을 리스트로 변환

        # 정답 배열에 추가하는 과정
        for p in range(len(c)):
            ans = ''
            for q in range(len(c[p])):
                ans += c[p][q]      # 쪼개져있는 문자열 합치기
            answer.append(ans)

    answer = sorted(answer)     # 오름차순 정렬

    return answer


if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
    # ["AC", "ACDE", "BCFG", "CDE"]

    print(solution( ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
    # ["ACD", "AD", "ADE", "CD", "XYZ"]

    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
    # ["WX", "XY"]

    print(solution(["ABCD", "ABCD", "ABCD"], [2,3,4]))
    # ['AB', 'ABC', 'ABCD', 'ABD', 'AC', 'ACD', 'AD', 'BC', 'BCD', 'BD', 'CD']