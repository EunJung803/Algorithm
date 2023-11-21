def solution(gems):
    answer = [0, len(gems) + 1]

    # 특정 범위 물건 모두 싹쓸이 구매
    # 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

    # 보석 종류 파악
    gem_type_cnt = len(list(set(gems)))

    left = 0
    right = 0

    gem_dict = dict()  # {보석종류 : 빈도수} 형태로 저장

    """투포인터"""
    while (right < len(gems)):
        # right를 움직이며 딕셔너리에 보석 담기 + 빈도수 업데이트 과정
        if (gems[right] not in gem_dict):
            gem_dict[gems[right]] = 1
        else:
            gem_dict[gems[right]] += 1
        right += 1

        # 딕셔너리에 담긴 보석 종류가 전체 보석 종류 개수와 같아진다면 -> left를 움직이며 최소 구간 찾기
        if (len(gem_dict) == gem_type_cnt):
            while (left < right):
                # 현재 left에 있는 보석의 출현 빈도수가 2 이상이라면
                if (gem_dict[gems[left]] > 1):  # 더 짧은 구간을 찾기 위해 right 근처로 left 이동
                    gem_dict[gems[left]] -= 1
                    left += 1
                # 현재 left~right 범위가 answer에 저장된 범위보다 짧다면
                elif (right - left < answer[1] - answer[0]):
                    answer = [left, right]  # answer 범위 업데이트
                    break
                # left를 이동하게 되었을 때 보석 종류가 줄어들게 되는 경우 ->  break
                else:
                    break

    answer[0] += 1  # answer와 범위 비교를 위해서 그냥 저장해뒀던 left를 정답 형식으로 변형 (문제에서는 인덱스가 1부터 시작하기 때문)
    return answer


if __name__ == '__main__':
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))  # [3, 7]

"""
### 효율성 실패 정답

from collections import Counter

def solution(gems):
    answer = []
    
    # 특정 범위 물건 모두 싹쓸이 구매
    # 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
    
    # 보석 종류 파악
    gem_type = list(set(gems))  
        
    n = len(gem_type)
    check_min = len(gems)   # 가장 짧은 구간인지 비교하기 위한 변수
    ans_list = []
    
    # 모든 종류가 들어있는 짧은 구간 찾기 (중간에 잘리면 X, 연속되는 구간 중 제일 짧은걸로)
    while(n <= len(gems)):
        keep = True
        # i부터 n만큼 슬라이싱해서 비교
        for i in range(len(gems)):
            flag = True
            if(i+n <= len(gems)):
                sub = gems[i:i+n]
                sub_count = Counter(sub)
                print(sub_count)
                if(len(sub_count) == len(gem_type)):
                    answer = [i+1, i+n]
                    keep = False
                    break
         # 조건에 충족하지 않는다면 슬라이싱 범위 늘리기
        if(keep):
            n += 1
        # 정답을 찾았다면 return
        if(keep == False):
            return answer
    
    return answer
"""
