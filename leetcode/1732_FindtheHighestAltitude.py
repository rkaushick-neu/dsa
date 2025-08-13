# 1732. Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# Difficulty: Easy

# Accepted: 510.5K
# Submissions: 610.1K
# Acceptance Rate: 83.7%

# Concept Prefix Sum

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest_altitude = current_altitude = 0
        for net_gain in gain:
            current_altitude += net_gain
            highest_altitude = current_altitude if(current_altitude > highest_altitude) else highest_altitude
        return highest_altitude

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    gain = [-5,1,5,0,-7]
    print('\nTest Case #1')
    print(f'solution.largestAltitude(gain={gain}) = {solution.largestAltitude(gain=gain)}')
    print('Expected Output: 1')

    # Test Case #2
    # Inputs:
    gain = [-4,-3,-2,-1,4,3,2]
    print('\nTest Case #2')
    print(f'solution.largestAltitude(gain={gain}) = {solution.largestAltitude(gain=gain)}')
    print('Expected Output: 0')
