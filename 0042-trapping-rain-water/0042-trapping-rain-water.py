class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)
        WaterStore = 0
        l_max, r_max = height[0], height[len(height)-1]

        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max, height[left])
                WaterStore += l_max - height[left]
            else:
                right -= 1
                r_max = max(r_max, height[right])
                WaterStore += r_max - height[right]

        return WaterStore