class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest =""
        l = len(s)
        # iterate the string, and explore every center
        def expand_center(s,l,left,right):
            while left >=0 and right <l and s[left] == s[right]:
                left -=1
                right +=1

            return s[left+1:right]
        
        for idx in range(l):
            # check the odd string
            odd_str =expand_center(s,l,idx,idx)
            if len(odd_str) > len(longest):
                longest = odd_str
            # check the even string
            even_str = expand_center(s,l,idx,idx+1)
            if len(even_str) > len(longest):
                longest = even_str
        
        return longest
