# 1493. Longest Subarray of 1's After Deleting One Element

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # keeping a flag b/c we must delete one element
        elementDeletedFlag = False
        max_1s = current_1s = l = 0
        n = len(nums)
        for i in range(0, n):
            # equivalent to if nums[i] == 1
            if(nums[i]):
                current_1s += 1
            # nums[i] == 0
            else:
                # if elementDeletedFlag == False
                if(not elementDeletedFlag):
                    elementDeletedFlag = True
                else:
                    # we've already deleted 0,
                    # so now we need to traverse l till the next 0
                    while(nums[l] != 0):
                        current_1s -= 1
                        l += 1
                    l += 1
            max_1s = current_1s if(current_1s > max_1s) else max_1s
        # after we finish if the element delete flag is still false
        # it means we haven't deleted any element
        # so we will delete a '1'
        if(not elementDeletedFlag):
            return max_1s-1
        else:
            return max_1s

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nums = [1,1,0,1]
    print('\nTest Case #1')
    print(f'solution.longestSubarray(nums={nums}) = {solution.longestSubarray(nums=nums)}')
    print('Expected Output: 3')

    # Test Case #2
    # Inputs:
    nums = [0,1,1,1,0,1,1,0,1]
    print('\nTest Case #2')
    print(f'solution.longestSubarray(nums={nums}) = {solution.longestSubarray(nums=nums)}')
    print('Expected Output: 5')

    # Test Case #3
    # Inputs:
    nums = [1,1,1]
    print('\nTest Case #3')
    print(f'solution.longestSubarray(nums={nums}) = {solution.longestSubarray(nums=nums)}')
    print('Expected Output: 2')

    # Test Case #4
    # Inputs:
    nums = [1]
    print('\nTest Case #4')
    print(f'solution.longestSubarray(nums={nums}) = {solution.longestSubarray(nums=nums)}')
    print('Expected Output: 0')

    # Test Case #5
    # Inputs:
    nums = [0]
    print('\nTest Case #5')
    print(f'solution.longestSubarray(nums={nums}) = {solution.longestSubarray(nums=nums)}')
    print('Expected Output: 0')

    print("\nLeetCode Runtime: 24ms")
    print("LeetCode Beats: 92.24%")