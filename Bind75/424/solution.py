class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # we could use slid window to solve the probem
        left =0
        l =len(s)
        char_count =[0 for _ in range(26)]
        max_char_count =0
        max_len =0
        for right in range(left,l):
            idx = ord(s[right])-ord("A")
            char_count[idx] +=1
            max_char_count =max(max_char_count,char_count[idx])
            if right -left+1-max_char_count > k:
                char_count[ord(s[left])-ord("A")] -=1
                left +=1

            max_len =max(max_len,right-left+1)
        return max_len