# 437. Path Sum III

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

from typing import Optional
import matplotlib.pyplot as plt
import numpy as np


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
    
    def visualize_tree(self):
        def get_tree_height(node):
            if not node:
                return 0
            return 1 + max(get_tree_height(node.left), get_tree_height(node.right))

        def get_tree_width(node):
            if not node:
                return 0
            return 1 + get_tree_width(node.left) + get_tree_width(node.right)

        def plot_tree(node, x, y, dx, level):
            if not node:
                return

            # Plot current node
            plt.plot(x, y, 'o', markersize=20, color='skyblue')
            plt.text(x, y, str(node.val), ha='center', va='center')

            # Calculate positions for children
            next_dx = dx / 2
            next_y = y - 1

            # Draw left child
            if node.left:
                next_x_left = x - dx
                plt.plot([x, next_x_left], [y, next_y], '-', color='gray')
                plot_tree(node.left, next_x_left, next_y, next_dx, level + 1)

            # Draw right child
            if node.right:
                next_x_right = x + dx
                plt.plot([x, next_x_right], [y, next_y], '-', color='gray')
                plot_tree(node.right, next_x_right, next_y, next_dx, level + 1)

        # Set up the plot
        plt.figure(figsize=(10, 8))
        height = get_tree_height(self)
        width = get_tree_width(self)
        
        # Plot the tree
        plot_tree(self, 0, 0, width/2, 1)
        
        # Adjust plot settings
        plt.axis('equal')
        plt.axis('off')
        plt.title('Binary Tree Visualization')
        plt.show()
    


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.countPaths = 0
        # cumulativeSumDict = {cumulativeSum: count}
        # we've seen 0 exactly once (not seen anything yet)
        self.cumulativeSumDict = {0: 1}
        def dfs(node: Optional[TreeNode], cumulativeSum: int, targetSum: int):

            # exit condition
            if(node is None):
                return

            cumulativeSum += node.val
            # current node compute the complement sum required: 
            complementSumRequired = cumulativeSum - targetSum

            # add the cumulativeSum to the dictionary
            if(cumulativeSum in self.cumulativeSumDict):
                self.cumulativeSumDict[cumulativeSum] += 1
            else:
                self.cumulativeSumDict[cumulativeSum] = 1

            # check if required cumulative sum is present in the cumulativeSumDict
            if(complementSumRequired in self.cumulativeSumDict):
                self.countPaths += self.cumulativeSumDict[complementSumRequired]

            # in case complementSumRequired == cumulativeSum: we count it twice
            # so reduce one in the count paths
            if(complementSumRequired == cumulativeSum):
                self.countPaths -= 1
            # check left
            dfs(node.left, cumulativeSum, targetSum)
            # check right
            dfs(node.right, cumulativeSum, targetSum)
            
            # backtrack remove the current node's contribution
            self.cumulativeSumDict[cumulativeSum] -= 1
            return 
        
        dfs(root, 0, targetSum)
        return self.countPaths
    

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nodes = [10,5,-3,3,2,None,11,3,-2,None,1]
    targetSum = 8
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #1')
    print(f'solution.pathSum({nodes}, {targetSum}) = {solution.pathSum(head, targetSum)}')
    print(f'Expected Output: 3')

    # Test Case #2
    # Inputs:
    nodes = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    targetSum = 22
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #2')
    print(f'solution.pathSum({nodes}, {targetSum}) = {solution.pathSum(head, targetSum)}')
    print(f'Expected Output: 3')

    # Test Case #3
    # Inputs:
    nodes = []
    targetSum = 8
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #3')
    print(f'solution.pathSum({nodes}, {targetSum}) = {solution.pathSum(head, targetSum)}')
    print(f'Expected Output: 0')

    # Test Case #4
    # Inputs:
    nodes = [10, -1, None, 1]
    targetSum = 10
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #4')
    print(f'solution.pathSum({nodes}, {targetSum}) = {solution.pathSum(head, targetSum)}')
    print(f'Expected Output: 2')

    # Test Case #5
    # Inputs:
    nodes = [1]
    targetSum = 0
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #5')
    print(f'solution.pathSum({nodes}, {targetSum}) = {solution.pathSum(head, targetSum)}')
    print(f'Expected Output: 0')
        

