class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l =len(s)
        nums = 0
        #  the idea is the same as the longest palindromic string, leecode 5
        def expand_center(s,l,left,right):
            cnt =0
            while left>=0 and right < l and s[left] == s[right]:
                left -=1
                right +=1
                cnt +=1
            return cnt
        
        for idx in range(l):
            odd_cnt = expand_center(s,l,idx,idx)
            even_cnt = expand_center(s,l,idx,idx+1)
            nums +=odd_cnt + even_cnt
        return nums