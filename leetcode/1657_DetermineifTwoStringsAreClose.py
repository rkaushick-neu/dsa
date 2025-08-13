# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# Difficulty: Medium

# Accepted: 422.9K
# Submissions: 781K
# Acceptance Rate: 54.2%

from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # edge case: if the lengths are not equal return false
        if(len(word1) != len(word2)):
            return False
        # create a hash-map of number of times a character occurs
        word1Dict, word2Dict = defaultdict(int), defaultdict(int)
        for ch in word1:
            word1Dict[ch] += 1
        for ch in word2:
            word2Dict[ch] += 1
        # create a set for word1 of keys & the same for word2
        word1SetKeys, word2SetKeys = set(), set()
        # create a list for word1 of occurrences & the same for word2
        word1SetOccurrences, word2SetOccurrences = [], []
        for key, occurrence in word1Dict.items():
            word1SetKeys.add(key)
            word1SetOccurrences.append(occurrence)
        for key, occurrence in word2Dict.items():
            word2SetKeys.add(key)
            word2SetOccurrences.append(occurrence)
        # sort both of them
        word1SetOccurrences.sort()
        word2SetOccurrences.sort()
        # if both sets (for key and values) are equal, we can return True, else False
        if((word1SetKeys == word2SetKeys) and (word1SetOccurrences == word2SetOccurrences)):
            return True
        return False
    

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    word1 = "abc"
    word2 = "bca"
    print('\nTest Case #1')
    print(f'solution.closeStrings(word1="{word1}", word2="{word2}") = {solution.closeStrings(word1=word1, word2=word2)}')
    print('Expected Output: True')

    # Test Case #2
    # Inputs:
    word1 = "a"
    word2 = "aa"
    print('\nTest Case #2')
    print(f'solution.closeStrings(word1="{word1}", word2="{word2}") = {solution.closeStrings(word1=word1, word2=word2)}')
    print('Expected Output: False')

    # Test Case #3
    # Inputs:
    word1 = "cabbba"
    word2 = "abbccc"
    print('\nTest Case #3')
    print(f'solution.closeStrings(word1="{word1}", word2="{word2}") = {solution.closeStrings(word1=word1, word2=word2)}')
    print('Expected Output: True')

    # Test Case #4
    # Inputs:
    word1 = "cccbbbaa"
    word2 = "cabbcccc"
    print('\nTest Case #4')
    print(f'solution.closeStrings(word1="{word1}", word2="{word2}") = {solution.closeStrings(word1=word1, word2=word2)}')
    print('Expected Output: False')

    # Test Case #5
    # Inputs:
    word1 = "cabbba"
    word2 = "deefff"
    print('\nTest Case #5')
    print(f'solution.closeStrings(word1="{word1}", word2="{word2}") = {solution.closeStrings(word1=word1, word2=word2)}')
    print('Expected Output: False')

    # Test Case #6
    # Inputs:
    word1 = "aaabbbbccddeeeeefffff"
    word2 = "aaaaabbcccdddeeeeffff"
    print('\nTest Case #6')
    print(f'solution.closeStrings(word1="{word1}", word2="{word2}") = {solution.closeStrings(word1=word1, word2=word2)}')
    print('Expected Output: False')

    print("\nLeetCode Runtime: 147ms")
    print("LeetCode Beats: 41.59%")