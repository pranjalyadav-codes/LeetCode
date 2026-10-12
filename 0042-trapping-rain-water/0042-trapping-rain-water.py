class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        water = 0

        while left < right :
            if height[left] <= height[right]:
                max_left = max(max_left, height[left])
                water += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                water += max_right - height[right]
                right -= 1
        return water
