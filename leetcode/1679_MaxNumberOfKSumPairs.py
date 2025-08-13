# 1679: Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Difficulty: Medium

# Accepted: 403.2K
# Submissions: 725.5K
# Acceptance Rate: 55.6%

class Solution:

    # Approach #1: Using 2 Pointers
    def maxOperations1(self, nums: list[int], k: int) -> int:
        count = 0
        # first sort the array
        nums.sort()
        # taking two pointers
        ptr1 = 0
        ptr2 = len(nums)-1
        while(ptr1 < ptr2):
            summed = nums[ptr1] + nums[ptr2]
            if(summed == k):
                count += 1
                # increment ptr1 & decrement ptr2
                ptr1 += 1
                ptr2 -= 1
            elif(summed < k):
                # result is lower than k, so just increment ptr1
                ptr1 += 1
            else:
                # result is higher than k, so just decrement ptr2
                ptr2 -= 1
        return count
    
    # Approach 2: Using a Complementary Dictionary
    def maxOperations2(self, nums: list[int], k: int) -> int:
        count = 0
        # first sort the array
        nums.sort()
        # taking two pointers
        ptr1 = 0
        ptr2 = len(nums)-1
        while(ptr1 < ptr2):
            summed = nums[ptr1] + nums[ptr2]
            if(summed == k):
                count += 1
                # increment ptr1 & decrement ptr2
                ptr1 += 1
                ptr2 -= 1
            elif(summed < k):
                # result is lower than k, so just increment ptr1
                ptr1 += 1
            else:
                # result is higher than k, so just decrement ptr2
                ptr2 -= 1
        return count

if __name__ == '__main__':
    solution = Solution()
    
    # Test Case #1
    # Inputs:
    nums = [1,2,3,4] 
    k = 5
    # Expected Output: 2
    print("Approach #1: Using 2 pointers:")
    print(f'Test Case 1: maxOperations1(nums={nums}, k={k}) = {solution.maxOperations1(nums=nums, k=k)}')
    print('Expected Output: 2')
    print()

    print("Approach #2: Using a Complementary Dictionary:")
    print(f'Test Case 1: maxOperations2(nums={nums}, k={k}) = {solution.maxOperations2(nums=nums, k=k)}')
    print('Expected Output: 2')
    print()

    # Test Case 2
    nums = [3,1,3,4,3]
    k = 6
    print("Approach #1: Using 2 pointers:")
    print(f'Test Case 2: maxOperations1(nums={nums}, k={k}) = {solution.maxOperations1(nums=nums, k=k)}')
    print('Expected Output: 1')
    print()

    print("Approach #2: Using a Complementary Dictionary:")
    print(f'Test Case 2: maxOperations2(nums={nums}, k={k}) = {solution.maxOperations2(nums=nums, k=k)}')
    print('Expected Output: 1')
    print()


    
