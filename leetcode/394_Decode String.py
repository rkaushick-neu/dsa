# 394. Decode String

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

class Solution:
    def decodeString(self, s: str) -> str:
        num_st = []
        char_st = []
        # we need current number (in case the number has more than 1 digit)
        current_number = 0
        for ch in s:
            if(ch.isnumeric()):
                current_number = current_number * 10 + int(ch)
            else:
                if(ch == ']'):
                    # pop until we find respective '[' (opening bracket)
                    new_str = char_st.pop()
                    while(char_st[-1] != '['):
                        # keep popping
                        # and changing the new_str
                        new_str = char_st.pop() + new_str
                    # now the top is '[', so we can pop once more
                    char_st.pop()
                    # next we have to pop the number
                    num_multiply = int(num_st.pop())
                    new_str = new_str * num_multiply
                    # add the new_str back to the char stack
                    char_st.append(new_str)
                elif(ch == '['):
                    # number is done - add it to num stack
                    # and set it back to 0
                    num_st.append(current_number)                    
                    current_number = 0
                    # add the '[' to the char stack
                    char_st.append(ch)
                else:
                    # anything other than '[' or ']'just add to the char stack
                    char_st.append(ch)
        # in the end, if there are some elements present in the stack,
        # we need to pop them and put them in reverse order
        new_str = ''
        while(len(char_st) != 0):
            new_str = char_st.pop() + new_str
        return new_str

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    s = "3[a]2[bc]"
    print('\nTest Case #1')
    print(f'solution.decodeString(s={s}) = {solution.decodeString(s=s)}')
    print(f'Expected Output: "aaabcbc"')

    # Test Case #2
    # Inputs:
    s = "3[a2[c]]"
    print('\nTest Case #2')
    print(f'solution.decodeString(s={s}) = {solution.decodeString(s=s)}')
    print(f'Expected Output: "accaccacc"')

    # Test Case #3
    # Inputs:
    s = "2[abc]3[cd]ef"
    print('\nTest Case #3')
    print(f'solution.decodeString(s={s}) = {solution.decodeString(s=s)}')
    print(f'Expected Output: "abcabccdcdcdef"')

    # Test Case #4
    # Inputs:
    s = "3[2[bc]]"
    print('\nTest Case #4')
    print(f'solution.decodeString(s={s}) = {solution.decodeString(s=s)}')
    print('Expected Output: "bcbcbcbcbcbc"')

    # Test Case #4
    # Inputs:
    s = "100[leetcode]"
    print('\nTest Case #4')
    print(f'solution.decodeString(s={s}) = {solution.decodeString(s=s)}')
    print('Expected Output Satisfied?')
    print("leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode" == solution.decodeString(s=s))