class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #  use slide window, left_idx, right_idx: first thought 
        # ==> lead to fail, since it can not solve the overlapping or contagious cases
        #  asked chatGPT, and was been told recursive is needed.
        #  below is an naive solution, without any optimization, memoization or bottom-top
        wordSet = set(wordDict)
        l= len(s)
        memo ={}
        def dfs(start):
            #  base case: if the start reach last, then it's true
            if start ==l:
                return True

            if start in memo:
                return memo[start]

            for end in range(start+1,l+1):
                sub_str = s[start:end]
                if sub_str in wordSet:
                    if dfs(end):
                        memo[start] =True
                        return True

            memo[start] =False
            return False
        
        return dfs(0)




