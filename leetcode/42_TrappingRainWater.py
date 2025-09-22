# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9


# Constraints:
#     n == height.length
#     1 <= n <= 2 * 104
#     0 <= height[i] <= 105

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        total_water = 0

        while left < right:
            if max_left < max_right:
                # move left once and check if it can store water
                left += 1
                max_left = max(max_left, height[left])
                total_water += (max_left - height[left])
            else:
                # move right once and check if it can store water
                right -= 1
                max_right = max(max_right, height[right])
                total_water += (max_right - height[right])
        
        return total_water

if __name__ == '__main__':
    solution = Solution()

    # Example 1:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    output = 6
    print('\nTest Case #1')
    print(f'solution.trap(height={height}) = {solution.trap(height=height)}')
    print(f'Expected Output: {output}')

    # Example 2:
    height = [4,2,0,3,2,5]
    output = 9
    print('\nTest Case #2')
    print(f'solution.trap(height={height}) = {solution.trap(height=height)}')
    print(f'Expected Output: {output}')

    # Example 3:
    height = [1]
    output = 0
    print('\nTest Case #3')
    print(f'solution.trap(height={height}) = {solution.trap(height=height)}')
    print(f'Expected Output: {output}')