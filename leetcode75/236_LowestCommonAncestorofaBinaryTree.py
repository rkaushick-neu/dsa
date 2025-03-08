# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
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
    
    # to print the node's value
    def __str__(self):
        return f'{self.val}'

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        common_ancestor_p, common_ancestor_q = [], []

        def dfs(node: 'TreeNode', e: 'TreeNode', e_list: list) -> bool:
            # print(f'node: {node}, e: {e}, e_list: {e_list}')
            # exit condition - no more nodes
            if(not node):
                return False
            # exit condition - when e is found
            if(node.val == e.val):
                # add it to the list
                e_list.append(node)
                # print(e_list)
                return True
            if(dfs(node.left, e, e_list) or dfs(node.right, e, e_list)):
                # add this to the list
                e_list.append(node)
                # print(e_list)
                return True

        # when we find the path from root to p, we store it in common_ancestor_p 
        dfs(node=root, e=p, e_list=common_ancestor_p)
        # when we find the path from root to q, we store it in common_ancestor_q
        dfs(node=root, e=q, e_list=common_ancestor_q)

        # now finding the least common ancestor:
        # print(common_ancestor_p)
        # print(common_ancestor_q)
        for n in common_ancestor_p:
            if(n in common_ancestor_q):
                # print(n)
                return n

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nodes = [3,5,1,6,2,0,8,None,None,7,4]
    p = TreeNode(5)
    q = TreeNode(1)
    head = TreeNode.buildTree(nodes)
    lca = solution.lowestCommonAncestor(head, p=p, q=q)
    print('\nTest Case #1')
    print(f'solution.lowestCommonAncestor({nodes}, p={p}, q={q}) = '), print(lca)
    print(f'Expected Output: 3')

    # Test Case #2
    # Inputs:
    nodes = [3,5,1,6,2,0,8,None,None,7,4]
    p = TreeNode(5)
    q = TreeNode(4)
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #2')
    print(f'solution.lowestCommonAncestor({nodes}, p={p}, q={q}) = {solution.lowestCommonAncestor(head, p=p, q=q)}')
    print(f'Expected Output: 5')

    # Test Case #3
    # Inputs:
    nodes = [1,2]
    p = TreeNode(1)
    q = TreeNode(2)
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #3')
    print(f'solution.lowestCommonAncestor({nodes}, p={p}, q={q}) = {solution.lowestCommonAncestor(head, p=p, q=q)}')
    print(f'Expected Output: 1')

    # Test Case #4
    # Inputs:
    nodes = [3,5,1,6,2,0,8,None,None,7,4]
    p = TreeNode(6)
    q = TreeNode(2)
    head = TreeNode.buildTree(nodes)
    print('\nTest Case #4')
    print(f'solution.lowestCommonAncestor({nodes}, p={p}, q={q}) = {solution.lowestCommonAncestor(head, p=p, q=q)}')
    print(f'Expected Output: 5')