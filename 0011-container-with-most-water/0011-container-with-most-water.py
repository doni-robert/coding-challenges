class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area with the current left and right pointers
            width = right - left
            area = min(height[left], height[right]) * width
            # Update max_area if a larger area is found
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area