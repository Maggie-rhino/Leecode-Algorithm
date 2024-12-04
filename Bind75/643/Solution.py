#  we should use start_idx, end_idx,sum_amt to capture the pattern
#  we should compare the avg of the window with the current item
import math


def findMaxAverage(self, nums: List[int], k: int) -> float:
    sum_max = float('-inf')
    l = len(nums)
    # init window
    sum_current =0
    for i in range(k):
        sum_current +=nums[i]
    sum_max = max(sum_current,sum_max)
    #  slide the window
    for j in range(k,l):
        sum_current = sum_current -nums[start_idx] +nums[j]
        if sum_current>=sum_max:
            sum_max = sum_current
    return sum_max/k

    