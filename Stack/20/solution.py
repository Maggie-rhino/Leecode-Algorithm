class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        pairs ={")":"(","]":"[","}":"{"}
        flag =True
        for c in s:
            if c in ("(","[","{"):
                stack.append(c)
            else:
                previous = stack.pop() if len(stack) else ""
                if pairs.get(c) !=previous:
                    flag =False
                    break
        if len(stack):
            flag =False
        return flag

