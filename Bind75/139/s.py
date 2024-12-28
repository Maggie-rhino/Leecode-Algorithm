class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)  # Convert the dictionary to a set for faster lookups

        def dfs(start):
            # Base Case: If we've reached the end of the string, return True
            if start == len(s):
                return True
            
            # Explore all possible prefixes
            for end in range(start + 1, len(s) + 1):  # `end` goes from `start + 1` to the end of the string
                prefix = s[start:end]  # Current prefix being checked
                if prefix in word_set:  # Check if the prefix is a valid word
                    # Recursively check the remaining substring
                    if dfs(end):  
                        return True
            
            # If no valid segmentation found, return False
            return False
        
        return dfs(0)  # Start DFS from the first character