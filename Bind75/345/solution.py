class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_idx =[]
        list_vowels =[]
        vowels =["a","e","i","o","u"]
        for idx in range(len(s)):
            c =s[idx]
            if c.lower() in vowels:
                list_idx.append(idx)
                list_vowels.append(c)
        l = len(list_idx)
        res =list(s)
        if l >0:
            for i in range(l):
                res[list_idx[i]] =list_vowels[l-i-1]
        return "".join(res)
        