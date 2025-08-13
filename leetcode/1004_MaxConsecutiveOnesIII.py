# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Difficulty: Medium

# Accepted: 802.8K
# Submissions: 1.2M
# Acceptance Rate: 64.8%

# Concept Sliding Window
# Achieved using 2 Pointers approach

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_count = current_count = j = 0
        n = len(nums)
        if(k == 0):
            for i in range(0, n):
                if(nums[i] == 0):
                    current_count = 0
                else:
                    current_count += 1
                max_count = current_count if (current_count > max_count) else max_count
            return max_count
        for i in range(0, n):
            if(nums[i] == 0 and k!=0):
                # flip from 0 to -1 and reduce the value of k
                nums[i] = -1
                k -= 1
                current_count += 1
            if(nums[i] == 1):
                current_count += 1
            if(nums[i] == 0 and k == 0):
                # move the j pointer until the next -1 spot
                nums[i] = -1
                while(nums[j]!=-1):
                    j += 1
                    current_count -= 1
                else:
                    # take that into consideration and move to the next
                    j += 1
            max_count = current_count if (current_count > max_count) else max_count
        return max_count
    
if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print('\nTest Case #1')
    print(f'solution.longestOnes(nums="{nums}", k={k}) = {solution.longestOnes(nums=nums, k=k)}')
    print('Expected Output: 6')

    # Test Case #2
    # Inputs:
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print('\nTest Case #2')
    print(f'solution.longestOnes(nums="{nums}", k={k}) = {solution.longestOnes(nums=nums, k=k)}')
    print('Expected Output: 10')

    # Test Case #3
    # Inputs:
    nums = [1,1,1,1,1]
    k = 5
    print('\nTest Case #3')
    print(f'solution.longestOnes(nums="{nums}", k={k}) = {solution.longestOnes(nums=nums, k=k)}')
    print('Expected Output: 5')

    # Test Case #4
    # Inputs:
    nums = [0,0,0,0,0]
    k = 3
    print('\nTest Case #4')
    print(f'solution.longestOnes(nums="{nums}", k={k}) = {solution.longestOnes(nums=nums, k=k)}')
    print('Expected Output: 3')

    # Test Case #5
    # Inputs:
    nums = [1,1,1,1,1,0,1]
    k = 0
    print('\nTest Case #5')
    print(f'solution.longestOnes(nums="{nums}", k={k}) = {solution.longestOnes(nums=nums, k=k)}')
    print('Expected Output: 5')

    print("\nLeetCode Runtime: 39ms")
    print("LeetCode Beats: 76.33%")