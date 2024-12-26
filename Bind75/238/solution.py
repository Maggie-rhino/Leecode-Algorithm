class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #  basic thought:
        #  use two list to store left product and right product except itself
        product_left =[]
        product_right =[]
        l =len(nums)
        # left product
        for idx in range(l):
            if idx ==0:
                product_left.append(1)
            else:
                v = nums[idx-1]
                product_left.append(product_left[-1]*v)
        # right product
        for idx in range(l-1,-1,-1):
            if idx == l-1:
                product_right.append(1)
            else:
                v = nums[idx+1]
                product_right.append(product_right[-1]*v)
        res=[]
        ll = len(product_left)
        for idx in range(ll):
            p=product_left[idx]* product_right[ll-idx-1]
            res.append(p)
        return res
            


