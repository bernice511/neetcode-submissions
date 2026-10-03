class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights)-1
        left = 0
        max_water = 0
        while left<right:
            breadth = right-left
            height = min(heights[left], heights[right])
            water = breadth*height
            max_water = max(max_water, water)
            if heights[left]<=heights[right]:
                left=left+1
            else:
                right = right-1
        return max_water



        