class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # use two pointer, left and right
        max_area = 0
        left =0
        right =len(height)-1
        while True:
            if left>=right:
                break
            h_left = height[left]
            h_right = height[right]
            area = (right-left) *min(h_left,h_right)
            max_area = max(area, max_area)
            if h_left <=h_right:
                left +=1
            else:
                right -=1
        return max_area
            
            
