class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = set(nums)
        for i in nums:
            hash_map[i] = i
        # iterate nums 
        longest_len =0
        for i in nums:
            next_ = i +1
            cur_len =1
            while next_ in hash_map.keys():
                cur_len +=1
                next_ +=1
            longest_len = max(longest_len,cur_len)
        return longest_len