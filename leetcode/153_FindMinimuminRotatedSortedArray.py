# 153. Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

 

# Constraints:

#     n == nums.length
#     1 <= n <= 5000
#     -5000 <= nums[i] <= 5000
#     All the integers of nums are unique.
#     nums is sorted and rotated between 1 and n times.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        # initially considering the left most as the smallest
        minimum = nums[left]
        while(left < right):
            if(nums[left] > nums[right]):
                minimum = nums[right]
                right -= 1
            else:
                break
        return minimum

if __name__ == '__main__':
    solution = Solution()

    # Example 1:
    nums = [3,4,5,1,2]
    output = 1
    print('\nTest Case #1')
    print(f'solution.findMin(nums="{nums}") = {solution.findMin(nums=nums)}')
    print(f'Expected Output: {output}')

    # Example 2:
    nums = [4,5,6,7,0,1,2]
    output = 0
    print('\nTest Case #2')
    print(f'solution.findMin(nums="{nums}") = {solution.findMin(nums=nums)}')
    print(f'Expected Output: {output}')

    # Example 3:
    nums = [11,13,15,17]
    output = 11
    print('\nTest Case #3')
    print(f'solution.findMin(nums="{nums}") = {solution.findMin(nums=nums)}')
    print(f'Expected Output: {output}')