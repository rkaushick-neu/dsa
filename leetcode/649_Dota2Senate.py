# 649. Dota2 Senate

# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # creating 2 queues - one for R & one for D
        num_senators = len(senate)
        r_queue = deque()
        d_queue = deque()
        for i in range(0, num_senators):
            r_queue.append(i) if(senate[i] == 'R') else d_queue.append(i)
        # until one of the queues becomes empty
        while(len(r_queue) > 0 and len(d_queue) > 0):
            r_index = r_queue.popleft()
            d_index = d_queue.popleft()
            if(r_index < d_index):
                # r get's priority & bans d
                # put r back to the next round (with an offset of n)
                r_queue.append(r_index + num_senators)
            else:
                # do the opposite otherwise
                d_queue.append(d_index + num_senators)
        if(len(r_queue) == 0):
            return "Dire"
        else:
            return "Radiant"
        

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    senate = "RD"
    print('\nTest Case #1')
    print(f'solution.predictPartyVictory(senate={senate}) = {solution.predictPartyVictory(senate=senate)}')
    print(f'Expected Output: "Radiant"')

    # Test Case #2
    # Inputs:
    senate = "RDD"
    print('\nTest Case #2')
    print(f'solution.predictPartyVictory(senate={senate}) = {solution.predictPartyVictory(senate=senate)}')
    print(f'Expected Output: "Dire"')

    # Test Case #3
    # Inputs:
    senate = "RRDD"
    print('\nTest Case #3')
    print(f'solution.predictPartyVictory(senate={senate}) = {solution.predictPartyVictory(senate=senate)}')
    print(f'Expected Output: "Radiant"')

    # Test Case #4
    # Inputs:
    senate = "DRRD"
    print('\nTest Case #4')
    print(f'solution.predictPartyVictory(senate={senate}) = {solution.predictPartyVictory(senate=senate)}')
    print('Expected Output: "Dire"')

    # Test Case #5
    # Inputs:
    senate = "DDRRR"
    print('\nTest Case #5')
    print(f'solution.predictPartyVictory(senate={senate}) = {solution.predictPartyVictory(senate=senate)}')
    print('Expected Output: "Dire"')

    # Test Case #6
    # Inputs:
    senate = "DDRRRR"
    print('\nTest Case #6')
    print(f'solution.predictPartyVictory(senate={senate}) = {solution.predictPartyVictory(senate=senate)}')
    print('Expected Output: "Radiant"')

    # Test Case #7
    # Inputs:
    senate = "RRDDDD"
    print('\nTest Case #7')
    print(f'solution.predictPartyVictory(senate={senate}) = {solution.predictPartyVictory(senate=senate)}')
    print('Expected Output: "Dire"')

    # Test Case #8
    # Inputs:
    senate = "RRRR"
    print('\nTest Case #8')
    print(f'solution.predictPartyVictory(senate={senate}) = {solution.predictPartyVictory(senate=senate)}')
    print('Expected Output: "Radiant"')
