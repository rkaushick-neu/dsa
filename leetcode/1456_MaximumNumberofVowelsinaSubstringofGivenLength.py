# 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Difficulty: Medium

# Accepted: 440.8K
# Submissions: 741.3K
# Acceptance Rate: 59.5%

# Concept Sliding Window
# Achieved using 2 Pointers approach

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        current_count = 0
        n = len(s)
        j = 0 # second pointer (k letters behind i)
        for i in range(0, n):
            # from 0 to k - keep counting the vowels
            if(i < k):
                # if letter is a vowel
                if(s[i] in 'aeiou'):
                    current_count += 1
            # from k to the end 
            else:
                if(s[j] in 'aeiou'):
                    # decrement current count (since we are losing one vowel)
                    current_count -= 1
                if(s[i] in 'aeiou'):
                    current_count += 1
                j += 1
            if(current_count == k):
                return current_count
            max_count = current_count if(current_count > max_count) else max_count
        return max_count
    
if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    s = "abciiidef"
    k = 3
    print('\nTest Case #1')
    print(f'solution.maxVowels(s="{s}", k={k}) = {solution.maxVowels(s=s, k=k)}')
    print('Expected Output: 3')

    # Test Case #2
    # Inputs:
    s = "aeiou"
    k = 2
    print('\nTest Case #2')
    print(f'solution.maxVowels(s="{s}", k={k}) = {solution.maxVowels(s=s, k=k)}')
    print('Expected Output: 2')

    # Test Case #3
    # Inputs:
    s = "leetcode"
    k = 3
    print('\nTest Case #3')
    print(f'solution.maxVowels(s="{s}", k={k}) = {solution.maxVowels(s=s, k=k)}')
    print('Expected Output: 2')

    # Test Case #4
    # Inputs:
    s = "abciideee"
    k = 3
    print('\nTest Case #4')
    print(f'solution.maxVowels(s="{s}", k={k}) = {solution.maxVowels(s=s, k=k)}')
    print('Expected Output: 3')

    # Test Case #5
    # Inputs:
    s = "weallloveyou"
    k = 7
    print('\nTest Case #5')
    print(f'solution.maxVowels(s="{s}", k={k}) = {solution.maxVowels(s=s, k=k)}')
    print('Expected Output: 4')