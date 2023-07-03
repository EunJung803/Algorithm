def making_weird_str(word):
    w = ''
    for i in range(len(word)):
        if(i % 2 == 0):
            w += word[i].upper()        # 짝수 인덱스 -> 대문자
        else:
            w += word[i].lower()        # 홀수 인덱스 -> 소문자

    return w

def solution(s):
    answer = ''

    splited_list = list(map(str, s.split(" ")))         # 문자열에서 공백을 기준으로 쪼개어 리스트로 변환

    count = 0
    for splited_word in splited_list:                    # 단어들이 들어있는 리스트를 돌며 각 단어를 함수로 변형하기
        weird_word = making_weird_str(splited_word)
        answer += weird_word        # 정답에 추가

        # 공백 관련 작업 처리
        # 출력할 정답 answer 맨 끝에 공백을 추가하지 않기 위해 마지막 단어를 변환할 경우를 제외하고는 모두 중간에 띄어쓰기용 공백 추가
        count += 1
        if(count != len(splited_list)):
            answer += ' '

    return answer

if __name__ == '__main__':
    print(solution("try hello world"))
    print(solution(" try hello world  d"))