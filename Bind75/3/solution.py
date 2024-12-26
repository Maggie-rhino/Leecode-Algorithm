class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        v_set = set()
        left =0
        l = len(s)
        right =0
        longest = 0
        while right < l:
            c = s[right]
            if c not in v_set:
                right +=1
                v_set.add(c)
            else:
                v_set.remove(s[left])
                left +=1
            longest = max(longest,right-left)
        return longest
        