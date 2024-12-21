class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1= len(str1)
        l2 = len(str2)
        idx =0
        longest_divisor =""
        while True:
            if idx >=l1 or idx >=l2:
                break 
            sub = str1[:idx+1]
            t1 = l1/(idx+1)
            t2= l2/(idx+1)
            s1 = sub* t1
            s2 = sub*t2
            if s1 ==str1 and s2 == str2:
                longest_divisor = sub if len(sub)>len(longest_divisor) else longest_divisor
            idx +=1
        return longest_divisor
        