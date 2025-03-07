# 1372. Longest ZigZag Path in a Binary Tree

# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildTree(arr: list) -> 'TreeNode':
        if not arr:
            return None
            
        root = TreeNode(arr[0])
        queue = [root]
        i = 1
        
        while queue and i < len(arr):
            node = queue.pop(0)
            # Add left child
            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1
            # Add right child
            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1
        return root

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_zig_zag = 0

        def dfs(node: Optional[TreeNode], goLeft: bool, count: int) -> None:
            # exit condition
            if(not node):
                return
            
            # check if the current node length is longer
            self.longest_zig_zag = max(self.longest_zig_zag, count)

            if(goLeft):
                # go left (and set goLeft to False, since we need to go right next)
                dfs(node.left, False, count+1)
                # check right node from count = 1
                dfs(node.right, True, 1)
            else:
                # go right
                dfs(node.right, True, count+1)
                dfs(node.left, False, 1)
        
        dfs(root, True, 0)
        return self.longest_zig_zag
    
if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nodes = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #1')
    print(f'solution.longestZigZag({nodes}) = {solution.longestZigZag(head)}')
    print(f'Expected Output: 3')

    # Test Case #2
    # Inputs:
    nodes = [1,1,1,None,1,None,None,1,1,None,1]
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #2')
    print(f'solution.longestZigZag({nodes}) = {solution.longestZigZag(head)}')
    print(f'Expected Output: 4')

    # Test Case #3
    # Inputs:
    nodes = [1]
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #3')
    print(f'solution.longestZigZag({nodes}) = {solution.longestZigZag(head)}')
    print(f'Expected Output: 0')
