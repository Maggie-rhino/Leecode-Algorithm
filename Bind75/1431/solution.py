class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        #  first, we need to find the current largest number 
        #  then compare the largest number with the current plus the extra candies
        max_sum = max(candies)
        res =[False] * len(candies)
        for i in candies:
            if candies[i] + extraCandies >= max_sum:
                res[i] =True
        return res
            