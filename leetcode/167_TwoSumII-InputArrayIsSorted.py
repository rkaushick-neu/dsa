# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

# Constraints:

# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.



class Solution:
    
    # taking the complement
    def twoSumComplement(self, numbers: list[int], target: int) -> list[int]:
        hash_set = {}
        for i, number in enumerate(numbers):
            if number in hash_set:
                return [hash_set[number], i+1]
            hash_set[target - number] = i+1
            # since it is 1-indexed
            # here index1 != index 2
            # and index1 will always be less than index2
            # we can end here since it is mentioned there will always be a valid solution
    

    # two pointers approach
    # time complexity: O(n)
    # space complexity O(1)
    def twoSumTwoPointers(self, numbers: list[int], target: int) -> list[int]:
        # two pointers approach
        left = 0
        right = len(numbers) - 1
        while(left < right):
            if(numbers[left] + numbers[right] > target):
                # decrement right
                right -= 1
            elif(numbers[left] + numbers[right] < target):
                # increment left
                left += 1 
            else:
                return [left+1, right+1]
            
if __name__ == '__main__':
    solution = Solution()

    print("Approach 1: Complement")
    # Test Case #1
    # Inputs:
    numbers = [2,7,11,15]
    target = 9
    print('\nTest Case #1')
    print(f'solution.twoSumComplement(numbers="{numbers}, target={target}") = {solution.twoSumComplement(numbers=numbers, target=target)}')
    print('Expected Output: [1,2]')

    # Test Case #2
    # Inputs:
    numbers = [2,3,4]
    target = 6
    print('\nTest Case #2')
    print(f'solution.twoSumComplement(numbers="{numbers}, target={target}") = {solution.twoSumComplement(numbers=numbers, target=target)}')
    print('Expected Output: [1,3]')

    # Test Case #3
    # Inputs:
    numbers = [-1,0]
    target = -1
    print('\nTest Case #3')
    print(f'solution.twoSumComplement(numbers="{numbers}, target={target}") = {solution.twoSumComplement(numbers=numbers, target=target)}')
    print('Expected Output: [1,2]')


    print("Approach 2: Two Pointers")
    # Test Case #1
    # Inputs:
    numbers = [2,7,11,15]
    target = 9
    print('\nTest Case #1')
    print(f'solution.twoSumTwoPointers(numbers="{numbers}, target={target}") = {solution.twoSumTwoPointers(numbers=numbers, target=target)}')
    print('Expected Output: [1,2]')

    # Test Case #2
    # Inputs:
    numbers = [2,3,4]
    target = 6
    print('\nTest Case #2')
    print(f'solution.twoSumTwoPointers(numbers="{numbers}, target={target}") = {solution.twoSumTwoPointers(numbers=numbers, target=target)}')
    print('Expected Output: [1,3]')

    # Test Case #3
    # Inputs:
    numbers = [-1,0]
    target = -1
    print('\nTest Case #3')
    print(f'solution.twoSumTwoPointers(numbers="{numbers}, target={target}") = {solution.twoSumTwoPointers(numbers=numbers, target=target)}')
    print('Expected Output: [1,2]')