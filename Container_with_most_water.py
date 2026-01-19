class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i<j:
            r = j - i
            mini = min(height[j], height[i])
            area = mini * r
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i+=1
            else:
                j -=1
            
        return max_area