def solution(citations):
    answer = 0

    # n편 중 h번 이상 인용된 논문이 h편 이상, h의 최댓값 구하기

    citations = sorted(citations)
    h = []

    for i in range(len(citations)):
        c_more = 0      # citations[i] 이상 인용된 논문의 개수를 담을 변수

        # citations[i]번 이상 인용된 논문의 개수 세기
        for j in citations:
            if(j >= citations[i]):
                c_more += 1

        if(c_more >= citations[i]):     # citations[i]번 이상 인용된 논문이 citations[i]편 이상일 때
            h.append(citations[i])      # -> h는 citations[i]
        else:                           # citations[i]번 이상 인용된 논문이 citations[i]편 이하일 때
            h.append(c_more)            # -> h는 c_more

    answer = max(h)     # 이런 모든 h들 중 최댓값이 정답

    return answer