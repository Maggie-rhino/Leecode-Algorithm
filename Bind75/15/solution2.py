class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        zeros, positive,negative =[],[],[]
        for num in nums:
            if num ==0:
                zeros.append(num)
            elif num >0:
                positive.append(num)
            else:
                negative.append(num)
        
        P =set(positive)
        N = set(negative)
        # case 1:
        if len(zeros)>=3:
            res.append([0,0,0])

        #  case 2
        if 0<len(zeros):
            for p in positive:
                if -p in negative:
                    sub_list =[-p,0,p]
                    if sub_list not in res:
                        res.append(sub_list)

        # case 3: two positive , one negative
        pl =len(positive)
        for i in range(pl):
            for j in range(i+1,pl):
                r = positive[i] + positive[j]
                if -r in N:
                    sub_list =[-r,positive[i],positive[j]]
                    sub_list.sort()
                    if sub_list not in res:
                        res.append(sub_list)
        #  case 4: two negative, one positive
        nl =len(negative)
        for i in range(nl):
            for j in range(i+1,nl):
                r = negative[i] + negative[j]
                if -r in P:
                    sub_list =[-r,negative[i],negative[j]]
                    sub_list.sort()
                    if sub_list not in res:
                        res.append(sub_list)
        
        return res
