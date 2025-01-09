class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # first we try brute force
        l =len(nums)
        res =[]
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if nums[i] + nums[j] + nums[k]==0:
                        sub_list =[nums[i],nums[j],nums[k]]
                        sub_list.sort()
                        if sub_list not in res:
                            res.append(sub_list)
        return res
    
                    
