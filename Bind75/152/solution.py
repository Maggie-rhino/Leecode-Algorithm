class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l =len(nums)
        if l==0:
            return 0

        max_p = nums[0]
        min_p =nums[0]
        res =nums[0]
        for idx in range(1,l):
            cur = nums[idx]
            if cur <0:
                max_p,min_p = min_p,max_P

            max_p =max(cur,cur*max_p)
            min_p =min(cur,cur*min_p)

            res =max(cur,max_p,res)
        return res


