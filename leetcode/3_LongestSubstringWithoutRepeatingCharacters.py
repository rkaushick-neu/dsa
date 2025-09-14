# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring
# without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge cases: if there are 0 or 1 characters in s
        if(len(s) <= 1):
            return len(s)

        left = 0
        right = 1

        hash_map = {}
        hash_map[s[left]] = left

        max_substring = 1

        while(right < len(s)):
            if(s[right] not in hash_map):
                hash_map[s[right]] = right
            else:
                # character has repeated in the hashmap
                # move left one more than the repeated character
                left = hash_map[s[right]] + 1
                # update the location of the repeated character
                hash_map[s[right]] = right

                # since we have moved left remove all the characters before left's location
                # not deleting while looping as that could cause issues
                keys_to_del = []
                for key, val in hash_map.items():
                    if(val < left):
                        keys_to_del.append(key)
                # now actually deleting those keys
                for key in keys_to_del:
                    del hash_map[key]
            
            # check if the dictionary is longer than max_substring
            if(len(hash_map) > max_substring):
                max_substring = len(hash_map)
            right += 1
        
        return max_substring

if __name__ == '__main__':
    solution = Solution()

    # Example 1:
    s = "abcabcbb"
    output = 3
    print('\nTest Case #1')
    print(f'solution.lengthOfLongestSubstring(s="{s}") = {solution.lengthOfLongestSubstring(s=s)}')
    print(f'Expected Output: {output}')

    # Example 2:
    s = "bbbbb"
    output = 1
    print('\nTest Case #2')
    print(f'solution.lengthOfLongestSubstring(s="{s}") = {solution.lengthOfLongestSubstring(s=s)}')
    print(f'Expected Output: {output}')

    # Example 3:
    s = "pwwkew"
    output = 3
    print('\nTest Case #3')
    print(f'solution.lengthOfLongestSubstring(s="{s}") = {solution.lengthOfLongestSubstring(s=s)}')
    print(f'Expected Output: {output}')

    # Example 4:
    s = "dvdf"
    output = 3
    print('\nTest Case #4')
    print(f'solution.lengthOfLongestSubstring(s="{s}") = {solution.lengthOfLongestSubstring(s=s)}')
    print(f'Expected Output: {output}')

    # Example 5:
    s = "aAbBcC"
    output = 6
    print('\nTest Case #5')
    print(f'solution.lengthOfLongestSubstring(s="{s}") = {solution.lengthOfLongestSubstring(s=s)}')
    print(f'Expected Output: {output}')