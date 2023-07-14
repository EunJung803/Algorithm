def solution(nums):
    pick_num = len(nums) // 2  # 뽑아야 하는 폰켓몬 수

    nums.sort()     # 정렬
    p = set()       # set() 선언

    # 리스트에 있는 폰켓몬을 하나씩 set에 넣어준다
    for i in nums:
        p.add(i)
        if (len(p) == pick_num):        # 뽑아야 하는 폰켓몬 수를 달성하면 -> 탈출
            break

    return len(p)


if __name__ == '__main__':
    print(solution([3,1,2,3]))
    print(solution([3,3,3,2,2,4]))
    print(solution([3,3,3,2,2,2]))
    print(solution([2,2]))
    print(solution([1,1,1,1]))



# 처음 생각했던 코드
'''
def solution(nums):
    pick_num = len(nums) // 2  # 뽑아야 하는 폰켓몬 수

    nums.sort()
    p = set()

    if(pick_num == 1):
        return 1

    for i in range(len(nums)-1):
        if(nums[i] != nums[i+1]):
            p.add(nums[i])
            p.add(nums[i+1])
        if(len(p) == pick_num):
            break

    if(len(p) == 0):
        return 1

    return len(p)

'''