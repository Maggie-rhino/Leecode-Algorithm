class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        previous =0
        v =0
        for i in range(l):
            if v >=n:
                return True
            current = flowerbed[i]
            next_ = 0 if i+1 >=l else flowerbed[i+1]
            if previous ==0 and current==0 and next_ ==0:
                v +=1
                previous =1
            else:
                previous = current
        return False if v <n else True