def solution(clothes):
    answer = 1

    cloths_comb = dict()

    for i in clothes:
        clothe = i[0]       # 옷 이름
        clothe_type = i[1]  # 옷의 종류
        if(clothe_type in cloths_comb):     # 딕셔너리에 이미 있는 종류라면
            cloths_comb[clothe_type].append(clothe)     # 해당 종류 value list에 추가
        else:   # 없는 새로운 종류라면
            cloths_comb[clothe_type] = [clothe]         # 새로운 value list 생성

    for clothe_type in cloths_comb.keys():      # 종류들만 꺼내봤을 때
        answer *= len(cloths_comb[clothe_type]) + 1     # 종류 안에 있는 value(옷) 개수 + 안입기(1)

    answer -= 1     # 모든 종류를 안입는 경우는 빼기
    print(answer)
    return answer

if __name__ == '__main__':
    solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
    solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
    solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])


# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

# cloths_comb = dict()
#
# for i in clothes:
#     clothe = i[0]
#     clothe_type = i[1]
#     if (clothe_type in cloths_comb):
#         cloths_comb[clothe_type].append(clothe)
#     else:
#         cloths_comb[clothe_type] = [clothe]
#
# print(cloths_comb)

# clothes_type = []
# clothes_comb = []
#
# # 각 옷의 종류를 겹치지 않게 담기
# for i in range(len(clothes)-1):
#     if (clothes[i][1] != clothes[i + 1][1]):
#         for j in range(i+1, len(clothes)):
#             if(clothes[i][1] != clothes[j][1]):
#                 clothes_type.append(clothes[i][1])
#                 break
#
# for i in range(len(clothes)):
#     clothes_comb.append(clothes[i][0])
#
# if(len(clothes_type) == 0):
#     clothes_type.append(clothes[0][1])
#     for i in range(len(clothes)):
#         clothes_comb.append(clothes[i][0])
#
# print(clothes_type)
# print(clothes_comb)