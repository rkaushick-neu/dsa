# 739. Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]


# Constraints:
#     1 <= temperatures.length <= 105
#     30 <= temperatures[i] <= 100

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [[temperatures[0], 0]]
        n = len(temperatures)
        result = [0] * len(temperatures)
        for i in range(1, n):
            while st and temperatures[i] > st[-1][0]:
                # need to pop the stack
                _, old_loc = st.pop()
                result[old_loc] = i-old_loc
            # now add the new temperature into the stack
            st.append([temperatures[i], i])
        return result

if __name__ == '__main__':
    solution = Solution()

    # Example 1:
    temperatures = [73,74,75,71,69,72,76,73]
    output = [1,1,4,2,1,1,0,0]
    print('\nTest Case #1')
    print(f'solution.dailyTemperatures(temperatures={temperatures}) = {solution.dailyTemperatures(temperatures=temperatures)}')
    print(f'Expected Output: {output}')

    # Example 2:
    temperatures = [30,40,50,60]
    output = [1,1,1,0]
    print('\nTest Case #2')
    print(f'solution.dailyTemperatures(temperatures={temperatures}) = {solution.dailyTemperatures(temperatures=temperatures)}')
    print(f'Expected Output: {output}')

    # Example 3:
    temperatures = [30,60,90]
    output = [1,1,0]
    print('\nTest Case #3')
    print(f'solution.dailyTemperatures(temperatures={temperatures}) = {solution.dailyTemperatures(temperatures=temperatures)}')
    print(f'Expected Output: {output}')