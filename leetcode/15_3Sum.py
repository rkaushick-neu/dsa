# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

 

# Constraints:

#     3 <= nums.length <= 3000
#     -105 <= nums[i] <= 105

 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if(i != 0 and nums[i] == nums[i-1]):
                continue
            j = i + 1
            k = n - 1
            while(j < k):
                if(nums[i] + nums[j] + nums[k] == 0):
                    res.append([nums[i], nums[j], nums[k]])
                    # check if the next one is the same as the prev
                    j += 1
                    while((nums[j] == nums[j-1]) and (j < k)):
                        # skip
                        j += 1
                elif(nums[i] + nums[j] + nums[k] < 0):
                    j += 1
                else:
                    k -= 1
        return res
    

if __name__ == '__main__':
    solution = Solution()

    # Example 1:
    nums = [-1,0,1,2,-1,-4]
    output = [[-1,-1,2],[-1,0,1]]
    print('\nTest Case #1')
    print(f'solution.threeSum(nums={nums}) = {solution.threeSum(nums=nums)}')
    print(f'Expected Output: {output}')

    # Example 2:
    nums = [0,1,1]
    output = []
    print('\nTest Case #2')
    print(f'solution.threeSum(nums={nums}) = {solution.threeSum(nums=nums)}')
    print(f'Expected Output: {output}')

    # Example 3:
    nums = [0,0,0]
    output = [[0,0,0]]
    print('\nTest Case #3')
    print(f'solution.threeSum(nums={nums}) = {solution.threeSum(nums=nums)}')
    print(f'Expected Output: {output}')
    
