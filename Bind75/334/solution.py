class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest = float('inf')
        second_smallest = float('inf')

        for num in nums:
            if num > second_smallest:
                return True
            if num < smallest:
                smallest = num
            elif   smallest <num < second_smallest :
                second_smallest = num
            
        return False