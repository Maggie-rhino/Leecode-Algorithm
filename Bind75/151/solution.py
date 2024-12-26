class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        previous = ""
        res = ""
        l = len(s)
        for c in s:
            if c ==" " and previous !="":
                res = previous +" "+ res
                previous =""
            elif c !=" ":
                previous +=c
        if previous !="":
            res = previous +" "+ res
        return res[:-1]
        