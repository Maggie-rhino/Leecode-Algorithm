class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l= len(nums)
        whole_set = set(nums)
        for cur in range(l):
            if cur not in whole_set:
                return cur
        return l

