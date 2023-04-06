class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = 0
        R = len(nums) - 1

        while (L <= R):
            mid = (L + R) // 2
            if (nums[mid] == target):
                return mid
            if (nums[mid] < target):  # target이 mid보다 오른쪽에 있으면
                L = mid + 1  # 오른쪽만 비교하기위해 L 이동
            else:
                R = mid - 1

        if ((target in nums) == False):  # target이 리스트에 존재하지 않는다면
            L2 = 0
            R2 = len(nums) - 1

            if (target < nums[0]):  # 가장 앞자리 수
                return 0

            if (target >= nums[-1]):  # 가장 뒷자리 수
                return len(nums)

            while (L2 <= R2):  # 둘 다 아니면 어느 자리에 들어갈지 다시 서칭
                mid = (L2 + R2) // 2
                if (nums[mid] <= target and nums[mid + 1] > target):  # 들어갈 자리 조건
                    return mid + 1
                if (nums[mid] < target):
                    L2 = mid + 1
                else:
                    R2 = mid - 1
