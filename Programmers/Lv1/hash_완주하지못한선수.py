def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            answer += participant[i]
            break

    if (answer == ''):
        answer += participant[-1]

    return answer

if __name__ == '__main__':
    solution(["leo", "kiki", "eden"], ["eden", "kiki"])
    solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
    solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
    solution(["mislav", "stanko", "mislav", "ana", "mislav", "mislav"], ["stanko", "ana", "mislav"])
