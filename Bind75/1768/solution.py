#  find the shorter string 

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res =''
        l1= len(word1)
        l2 = len(word2)
        s1= 0
        s2=0
        while True:
            if s1 <l1:
                res +=word1[s1]
            if s2 <l2:
                res +=word2[s2]
            if s1 >=l1-1 and s2 >=l2-1:
                break
            s1 +=1
            s2 +=1
        return res
    


                

        