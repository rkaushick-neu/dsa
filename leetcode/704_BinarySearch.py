# 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
 

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

from typing import List

class Solution:

    def search_recursive(self, nums: List[int], target: int) -> int:

        def binary_search(left_idx: int, right_idx: int):
            # exit condition: target not found
            if left_idx > right_idx:
                return -1
            mid = (left_idx+right_idx)//2
            # exit condition: target found
            if nums[mid] == target:
                return mid            
            if target > nums[mid]:
                # need to search from mid+1 to right
                return binary_search(mid+1, right_idx)
            else:
                # search from left to mid
                return binary_search(left_idx, mid-1)
            
        return binary_search(0, len(nums)-1)

    def search_iterative(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2
            # exit condition: target found
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                # search the second half
                left = mid+1
            else:
                # search the first half
                right = mid-1

        return -1

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nums = [-1,0,3,5,9,12]
    target = 9
    print('\nTest Case #1')
    print('Using recursion:')
    print(f'\tsolution.search_recursive(nums="{nums}, target={target}") = {solution.search_recursive(nums=nums, target=target)}')
    print('Using iterative approach:')
    print(f'\tsolution.search_iterative(nums="{nums}, target={target}") = {solution.search_iterative(nums=nums, target=target)}')
    print('Expected Output: 4')

    # Test Case #2
    # Inputs:
    nums = [-1,0,3,5,9,12]
    target = 2
    print('\nTest Case #2')
    print('Using recursion:')
    print(f'\tsolution.search_recursive(nums="{nums}, target={target}") = {solution.search_recursive(nums=nums, target=target)}')
    print('Using iterative approach:')
    print(f'\tsolution.search_iterative(nums="{nums}, target={target}") = {solution.search_iterative(nums=nums, target=target)}')
    print('Expected Output: -1')

    # Test Case #3
    # Inputs:
    nums = [-1,0,3,5,9,12]
    target = 0
    print('\nTest Case #3')
    print('Using recursion:')
    print(f'\tsolution.search_recursive(nums="{nums}, target={target}") = {solution.search_recursive(nums=nums, target=target)}')
    print('Using iterative approach:')
    print(f'\tsolution.search_iterative(nums="{nums}, target={target}") = {solution.search_iterative(nums=nums, target=target)}')
    print('Expected Output: 1')