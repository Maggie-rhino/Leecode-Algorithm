#  use one pointer to record the number of Zeros
#  use the other pointer to trace the position of the latest insert spot
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_z =0
        idx_insert =0
        l= len(nums)
        # edge case:
        if l ==1:
            return

        for i in range(l):
            current=nums[i]
            if current ==0:
                n_z +=1
            else:
                nums[idx_insert]= current
                idx_insert +=1
            if idx_insert+ n_z >=l:
                break
        for i in range(idx_insert,l):
            nums[i] =0            

