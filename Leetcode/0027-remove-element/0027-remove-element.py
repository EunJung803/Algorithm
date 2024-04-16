class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        n = nums.count(val)
        for i in range(n):
            nums.remove(val)

        k = len(nums)
        return k