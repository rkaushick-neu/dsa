# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

# Constraints:
#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        nums_set = set(nums)

        for num in nums_set:
            # first checking if it is the start of the sequence
            if num-1 not in nums_set:
                # this is the start because num-1 is not present
                seq = 1
                # check the next number
                next_num = num+1
                while next_num in nums_set:
                    seq += 1
                    next_num += 1
                # check if the length of the sequence is more than max_seq
                max_seq = seq if seq > max_seq else max_seq
            else:
                # not the start so check the next num
                pass
        
        return max_seq

if __name__ == '__main__':
    solution = Solution()

    # Example 1:
    nums = [100,4,200,1,3,2]
    output = 4
    print('\nTest Case #1')
    print(f'solution.longestConsecutive(nums={nums}) = {solution.longestConsecutive(nums=nums)}')
    print(f'Expected Output: {output}')

    # Example 2:
    nums = [0,3,7,2,5,8,4,6,0,1]
    output = 9
    print('\nTest Case #2')
    print(f'solution.longestConsecutive(nums={nums}) = {solution.longestConsecutive(nums=nums)}')
    print(f'Expected Output: {output}')

    # Example 3:
    nums = [1,0,1,2]
    output = 3
    print('\nTest Case #3')
    print(f'solution.longestConsecutive(nums={nums}) = {solution.longestConsecutive(nums=nums)}')
    print(f'Expected Output: {output}')

    # Example 4:
    nums = [100,200,3]
    output = 1
    print('\nTest Case #4')
    print(f'solution.longestConsecutive(nums={nums}) = {solution.longestConsecutive(nums=nums)}')
    print(f'Expected Output: {output}')

    # Example 5:
    nums = []
    output = 0
    print('\nTest Case #5')
    print(f'solution.longestConsecutive(nums={nums}) = {solution.longestConsecutive(nums=nums)}')
    print(f'Expected Output: {output}')