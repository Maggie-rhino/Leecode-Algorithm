class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)- set(nums2)
        set_2 =set(nums2) -set(nums1)
        return [list(set_1),list(set_2)]
        # write from scratch
