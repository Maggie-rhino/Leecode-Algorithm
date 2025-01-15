class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # start from middle, 
        # always compare the first, middle and last element
        #  to determin which way to go
        # case 1: middle is the biggest: go right
        # case 2: middle is the smallest: go left
        # case 3: middle is bigger than left but smaller than right: go left
        # [1,2,3,4,5]
        right = len(nums)-1
        left =0
        middle = (right-left)//2
        res_min =float('inf')
        while True:
            res_min =min(nums[right],nums[left],nums[middle],res_min)
            if right-left<=1:
                break
            if nums[middle] > nums[left] and nums[middle] >nums[right]:
                left =middle
                middle = (right-left)//2 +left
            else:
                right =middle
                middle =(right-left)//2 + left
        return res_min