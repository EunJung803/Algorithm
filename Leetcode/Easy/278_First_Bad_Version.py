# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        L = 0   # fronthead False (First F) == first bad one
        R = n   # latest True (just before the bad one)

        while L < R:
            mid = (L + R) // 2

            if isBadVersion(mid):
                R = mid
            else:
                L = mid + 1

        return L
