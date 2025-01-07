# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Difficulty: Easy

# Accepted: 1.3M
# Submissions: 2.1M
# Acceptance Rate: 59.4%

# Concept: Prefix Sum

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # first compute the sum
        sum_nums = 0
        # time: O(n)
        for num in nums:
            sum_nums +=  num
        current_left_sum = 0 # initially it is zero
        current_right_sum = sum_nums
        # time: O(n)
        for index, num in enumerate(nums):
            # remove the current number from the right sum
            current_right_sum -= num
            # add the previous number to the left sum (when it is not the 0th index)
            if(index != 0):
                current_left_sum += nums[index-1]
            # check if it right sum = left sum
            if(current_right_sum == current_left_sum):
                return index
        # when there is no pivot
        return -1
    
if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nums = [1,7,3,6,5,6]
    print('\nTest Case #1')
    print(f'solution.pivotIndex(nums="{nums}") = {solution.pivotIndex(nums=nums)}')
    print('Expected Output: 3')

    # Test Case #2
    # Inputs:
    nums = [1,2,3]
    print('\nTest Case #2')
    print(f'solution.pivotIndex(nums="{nums}") = {solution.pivotIndex(nums=nums)}')
    print('Expected Output: -1')

    # Test Case #3
    # Inputs:
    nums = [2,1,-1]
    print('\nTest Case #3')
    print(f'solution.pivotIndex(nums="{nums}") = {solution.pivotIndex(nums=nums)}')
    print('Expected Output: 0')