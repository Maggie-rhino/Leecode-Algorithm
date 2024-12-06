class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # first we use a hashmap to count the occurance of each value
        #  then we compare the count value to find duplication
        flag =True
        # step 1
        cnt_dict ={}
        for i in arr:
            v=1
            if i in cnt_dict.keys():
                v = cnt_dict[i]+1
            cnt_dict[i] =v
        
        # setp 2 :
        set_ = set(cnt_dict.values())
        if len(set_) < len(cnt_dict.values()):
            flag =False
        return flag

