from itertools import product

def solution(users, emoticons):
    answer = [0, 0]

    # 할인율에 따라 각 유저의 구매 이모티콘, 금액, + 가입 여부 확인
    # 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됨
    # 최대할인부터 내려가기

    sale = [0.4, 0.3, 0.2, 0.1]

    product_emo = list(product(emoticons, sale))    # (이모티콘, 할인율)의 모든 조합
    # print(product_emo)

    n = len(sale)   # 4
    split_product_emo = list(product_emo[i * n : (i + 1) * n] for i in range((len(product_emo) + n - 1) // n))      # 이모티콘 종류 별로 쪼개놓기
    # print(split_product_emo)

    new_product_emo = list(product(*split_product_emo))     # 쪼개놓은 것들 중 하나씩 뽑아서 각 (이모티콘, 할인율) 의 모든 조합을 담은 리스트
    # print(new_product_emo)

    # 해당 리스트를 하나씩 돌면서 판단
    for i in range(len(new_product_emo)):
        emoticon_plus = 0           # 이모티콘 플러스 가입자
        total_emoticon_value = 0    # 총 이모티콘 판매액
        for j in range(len(users)):         # 각 유저가 사게 될 이모티콘 금액을 구하기 (각 유저 구성요소 : [비율, 가격])
            user_spend = 0
            for e in range(len(emoticons)):
                sale_prise = new_product_emo[i][e][0] * (1 - new_product_emo[i][e][1])      # 유저가 사게되는 금액
                if(users[j][0] <= new_product_emo[i][e][1] * 100):      # 만약 '비율'% 이상의 할인이 있는 이모티콘이면 유저가 사게 됨
                    user_spend += sale_prise
            if(user_spend >= users[j][1]):      # 만약 '가격' 이상의 돈을 이모티콘 구매에 사용한다면 이모티콘 플러스 가입
                emoticon_plus += 1
            else:       # 이모티콘 플러스에 가입하지 않으면 총 이모티콘 가격 판매액만 업데이트
                total_emoticon_value += user_spend

        if(answer[0] < emoticon_plus):      # 이모티콘 플러스 가입자를 최대한 늘리는게 우선 목표이므로, 만약 더 많은 가입자를 얻은 답이 나오면 answer 변경
            answer = [emoticon_plus, total_emoticon_value]
        if (answer[0] == emoticon_plus):    # 그러나 같은 조건이라면, 다음 목표인 판매액 금액으로 비교
            if(answer[1] < total_emoticon_value):       # 이모티콘 플러스 가입자가 동일할 때, 판매액이 더 높다면 answer 변경
                answer = [emoticon_plus, total_emoticon_value]

    return answer

if __name__ == '__main__':
    print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
    print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))