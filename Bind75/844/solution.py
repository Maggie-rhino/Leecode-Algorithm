class Solution(object):

    def builtStack(self,string):
        stack =[]
        for c in string:
            if c !="#":
                stack.append(c)
            else:
                if len(stack):
                    stack.pop()
        return stack


    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = self.builtStack(s)
        stack_t = self.builtStack(t)
        if stack_s ==stack_t:
            return True
        return False