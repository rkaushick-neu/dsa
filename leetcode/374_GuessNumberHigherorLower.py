# 374. Guess Number Higher or Lower

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Since LeetCode has not shared the API for the guess method, I have defined it with the same meaning:
def guess(num: int) -> int:
    global pick
    if(num == pick):
        return 0
    elif(num > pick):
        return -1
    else: 
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        if(n == 1):
            return 1
        low = 1
        high = n
        mid = (low+high)//2
        while(guess(mid) != 0):  
            # our pick is higher (num is lower)
            if(guess(mid) == -1):
                high = mid-1
            else:
                low = mid+1
            mid = (low+high)//2
        return mid

if __name__ == '__main__':
    global pick
    solution = Solution()

    # Test Case #1
    # Inputs:
    n = 10
    pick = 6
    print('\nTest Case #1')
    print(f'solution.guessNumber(n={n}) = {solution.guessNumber(n=n)}')
    print(f'Expected Output: {pick}')

    # Test Case #2
    # Inputs:
    n = 1
    pick = 1
    print('\nTest Case #2')
    print(f'solution.guessNumber(n={n}) = {solution.guessNumber(n=n)}')
    print(f'Expected Output: {pick}')

    # Test Case #3
    # Inputs:
    n = 2
    pick = 1
    print('\nTest Case #3')
    print(f'solution.guessNumber(n={n}) = {solution.guessNumber(n=n)}')
    print(f'Expected Output: {pick}')

    # Test Case #4
    # Inputs:
    n = 2
    pick = 2
    print('\nTest Case #4')
    print(f'solution.guessNumber(n={n}) = {solution.guessNumber(n=n)}')
    print('Expected Output: 2')

    print("\nLeetCode Runtime: 35ms")
    print("LeetCode Beats: 60.68%")