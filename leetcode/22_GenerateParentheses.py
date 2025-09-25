# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]


# Constraints:
#     1 <= n <= 8

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # function within a function because it can access all the variables within the parent function (generateParenthesis())
        def gen_parents(parenthesis_string: str, n: int):
            if parenthesis_string.count("(") == n:
                # there are n number of opening brackets '('
                # Check if there are n number of closing brackets ')'
                if parenthesis_string.count(")") == n:
                    # add it to the list of parenthesis & DONE (exit)
                    parenthesis_list.append(parenthesis_string)
                    return
                else:
                    # add the closing bracket ')' and recursively call fn
                    gen_parents(parenthesis_string+")", n)
            else:
                # there are less than n number of opening brackets
                # add an extra opening bracket '(' and recursively call fn
                gen_parents(parenthesis_string+"(", n)
                # if number of opening brackets is more than number of closing brackets then add the closing bracket
                if parenthesis_string.count("(") > parenthesis_string.count(")"):
                    # add the closing bracket ')' and recursively call fn
                    gen_parents(parenthesis_string+")", n)
                else:
                    # do nothing (not well-formed)
                    pass
        
        parenthesis_list = []
        gen_parents("(", n)
        return parenthesis_list
            
if __name__ == '__main__':
    solution = Solution()

    # Example 1:
    n = 3
    output = ["((()))","(()())","(())()","()(())","()()()"]
    print('\nTest Case #1')
    print(f'solution.generateParenthesis(n={n}) = {solution.generateParenthesis(n=n)}')
    print(f'Expected Output: {output}')
    if solution.generateParenthesis(n=n) == output:
        print("Result matches expected output.")

    # Example 2:
    n = 1
    output = ["()"]
    print('\nTest Case #2')
    print(f'solution.generateParenthesis(n={n}) = {solution.generateParenthesis(n=n)}')
    print(f'Expected Output: {output}')
    if solution.generateParenthesis(n=n) == output:
        print("Result matches expected output.")
