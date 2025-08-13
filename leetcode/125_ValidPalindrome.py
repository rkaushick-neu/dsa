# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # only need alpha numeric
        s = s.lower()
        s = "".join([s[i] for i in range(len(s)) if s[i].isalnum()])
        # reverse the string and check if they are the same
        return s == s[::-1]
    
if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    s = "A man, a plan, a canal: Panama"
    print('\nTest Case #1')
    print(f'solution.isPalindrome(s="{s}") = {solution.isPalindrome(s=s)}')
    print('Expected Output: True')

    # Test Case #2
    # Inputs:
    s = "race a car"
    print('\nTest Case #2')
    print(f'solution.isPalindrome(s="{s}") = {solution.isPalindrome(s=s)}')
    print('Expected Output: False')

    # Test Case #3
    # Inputs:
    s = " "
    print('\nTest Case #3')
    print(f'solution.isPalindrome(s="{s}") = {solution.isPalindrome(s=s)}')
    print('Expected Output: True')