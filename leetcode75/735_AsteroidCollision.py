# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        result = []
        for index, asteroid in enumerate(asteroids):
            if(index == 0):
                result.append(asteroid)
                continue
            prev_asteroid = result[-1] if (len(result) > 0) else None
            if(prev_asteroid is None):
                # add asteroid to the result
                result.append(asteroid)
                continue
            # if both are in the same direction (+, +) or (-, -), then just add them to the list
            if((prev_asteroid > 0 and asteroid > 0) or (prev_asteroid < 0 and asteroid < 0)):
                result.append(asteroid)
            else:
                # both in different directions (+, -) or (-, +)
                # prev - positive, and the new one negative
                if((prev_asteroid > 0) and (asteroid < 0)):
                    # check if
                        # 1. they are the same size
                            # then they cancel each other out; remove the previous and move on
                        # 2. previous one is bigger --> it stays
                            # move on
                        # 3. previous one is smaller 
                            # --> it get's removed and then recursively check again from the check condition

                    while(True):
                        if(abs(prev_asteroid) == abs(asteroid) and (prev_asteroid > 0)):
                            result.pop()
                            break
                        elif(prev_asteroid < 0):
                            # prev one is now negative and asteroid is negative (-, -) so add it and break
                            result.append(asteroid)
                            break
                        elif(abs(prev_asteroid) > abs(asteroid)):
                            break
                        else:
                            result.pop()
                            if(len(result) > 0):
                                prev_asteroid = result[-1]
                            else:
                                result.append(asteroid)
                                break
                # else: prev - negative and the new one is positive
                else:
                    # previous is already left and doesn't collide 
                    # so add the new one in result:
                    result.append(asteroid)
        return result

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    asteroids = [5,10,-5]
    print('\nTest Case #1')
    print(f'solution.asteroidCollision(asteroids={asteroids}) = {solution.asteroidCollision(asteroids=asteroids)}')
    print('Expected Output: [5,10]')

    # Test Case #2
    # Inputs:
    asteroids = [8,-8]
    print('\nTest Case #2')
    print(f'solution.asteroidCollision(asteroids={asteroids}) = {solution.asteroidCollision(asteroids=asteroids)}')
    print('Expected Output: []')

    # Test Case #3
    # Inputs:
    asteroids = [10,2,-5]
    print('\nTest Case #3')
    print(f'solution.asteroidCollision(asteroids={asteroids}) = {solution.asteroidCollision(asteroids=asteroids)}')
    print('Expected Output: [10]')

    # Test Case #4
    # Inputs:
    asteroids = [-2,-1,1,2]
    print('\nTest Case #4')
    print(f'solution.asteroidCollision(asteroids={asteroids}) = {solution.asteroidCollision(asteroids=asteroids)}')
    print('Expected Output: [-2,-1,1,2]')

    # Test Case #5
    # Inputs:
    asteroids = [-4,6]
    print('\nTest Case #5')
    print(f'solution.asteroidCollision(asteroids={asteroids}) = {solution.asteroidCollision(asteroids=asteroids)}')
    print('Expected Output: [-4,6]')

    # Test Case #6
    # Inputs:
    asteroids = [4,-6]
    print('\nTest Case #6')
    print(f'solution.asteroidCollision(asteroids={asteroids}) = {solution.asteroidCollision(asteroids=asteroids)}')
    print('Expected Output: [-6]')

    # Test Case #7
    # Inputs:
    asteroids = [-2,-2,1,-2]
    print('\nTest Case #7')
    print(f'solution.asteroidCollision(asteroids={asteroids}) = {solution.asteroidCollision(asteroids=asteroids)}')
    print('Expected Output: [-2,-2,-2]')

    # Test Case #8
    # Inputs:
    asteroids = [-2,-2,1,-1]
    print('\nTest Case #8')
    print(f'solution.asteroidCollision(asteroids={asteroids}) = {solution.asteroidCollision(asteroids=asteroids)}')
    print('Expected Output: [-2,-2]')

    print("\nLeetCode Runtime: 10ms")
    print("LeetCode Beats: 20.04%")