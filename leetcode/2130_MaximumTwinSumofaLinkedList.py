# 2130. Maximum Twin Sum of a Linked List

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def build_linked_list(values: list[int]):
        if(len(values) == 0):
            return None
        head = ListNode(values[0])
        current = head
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
        return head


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # count the number of nodes
        count = 0
        max_sum = 0
        node = head
        while(node):
            count += 1
            node = node.next
        node = head
        i = 1
        middle = int(count/2)
        node_values_dict = {}
        # a dictionary stores values of nodes from 1 to count/2
        while(i <= middle):
            node_values_dict[i] = node.val
            node = node.next
            i += 1
        # from (count/2)+1 to count --> add the corresponding twin
        while(i <= count):
            twin = count - i + 1
            twin_sum = node_values_dict[twin] + node.val
            if(twin_sum > max_sum):
                max_sum = twin_sum
            node = node.next
            i += 1
        return max_sum
    
if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nodes = [5,4,2,1]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #1')
    print(f'solution.pairSum(head={nodes}) = {solution.pairSum(head)}')
    print(f'Expected Output: {6}')

    # Test Case #2
    # Inputs:
    nodes = [4,2,2,3]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #2')
    print(f'solution.pairSum(head={nodes}) = {solution.pairSum(head)}')
    print(f'Expected Output: {7}')

    # Test Case #3
    # Inputs:
    nodes = [1,100000]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #3')
    print(f'solution.pairSum(head={nodes}) = {solution.pairSum(head)}')
    print(f'Expected Output: {100001}')

    # Test Case #4
    # Inputs:
    nodes = [4,2,3,4,5,5]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #4')
    print(f'solution.pairSum(head={nodes}) = {solution.pairSum(head)}')
    print(f'Expected Output: {9}')