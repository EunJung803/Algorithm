import math

def solution(progresses, speeds):
    answer = []

    # ([작업 진도], [개발 속도])
    # 첫번째 기능 -> 두번째 기능 -> 세번째 기능
    # 각 배포에 몇개의 기능이 배포되는지 return

    # 각 기능 개발에 어느정도의 기간이 걸리는지 개산하여 release_arr에 append
    release_arr = []
    for i in range(len(progresses)):
        release_arr.append(math.ceil((100 - progresses[i]) / speeds[i]))

    # release_arr을 돌면서 하나씩 꺼내면서 꺼낸 요소와 남아있는 요소를 순서대로 비교하기
    for j in range(len(release_arr)):
        if (len(release_arr) == 0):     # 비어있다면 break
            break

        count = 1
        tmp = release_arr.pop(0)    # 맨 앞 요소부터 꺼내어 비교하기

        # 비어있지 않을 때까지 배열 돌기
        while (release_arr):
            r = release_arr[0]      # 맨 앞 요소를 꺼냈으니 현재 0번째 인덱스는 꺼낸 맨 앞 요소의 바로 다음 요소
            if (r <= tmp):          # 만약 앞 기능의 개발 기간이 더 오래 걸린다면 -> 이번 기능은 그 앞 기능이 완료된 후 나올 수 있으므로 count + 1
                count += 1
                release_arr.pop(0)
            else:
                break

        answer.append(count)

    return answer