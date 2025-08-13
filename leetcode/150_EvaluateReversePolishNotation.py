# 150. Evaluate Reverse Polish Notation

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 

# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        num_stack = []
        for token in tokens:
            try:
                number = int(token)
                num_stack.append(number)
            except:
                last_num = num_stack.pop()
                second_last_num = num_stack.pop()
                if(token == '+'):
                    result = second_last_num + last_num
                elif(token == '-'):
                    result = second_last_num - last_num
                elif(token == '*'):
                    result = second_last_num * last_num
                elif(token == '/'):
                    result = int(second_last_num/last_num)
                num_stack.append(result)
        return num_stack[0]
    
if __name__ == '__main__':
    solution = Solution()

    # Example 1:

    tokens = ["2","1","+","3","*"]
    output = 9
    print('\nTest Case #1')
    print(f'solution.evalRPN(tokens="{tokens}") = {solution.evalRPN(tokens=tokens)}')
    print(f'Expected Output: {output}')


    tokens = ["4","13","5","/","+"]
    output = 6
    print('\nTest Case #2')
    print(f'solution.evalRPN(tokens="{tokens}") = {solution.evalRPN(tokens=tokens)}')
    print(f'Expected Output: {output}')

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    output = 22
    print('\nTest Case #3')
    print(f'solution.evalRPN(tokens="{tokens}") = {solution.evalRPN(tokens=tokens)}')
    print(f'Expected Output: {output}')