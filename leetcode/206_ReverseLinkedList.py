# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.
 
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

from typing import Optional

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

    def print_linked_list_as_list(head) -> list[int]:
        current = head
        values = []
        while(current is not None):
            values.append(current.val)
            current = current.next
        return values

class Solution:
    # iterative approach
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if(head is None or head.next is None):
            return head
        
        first = head
        second = first.next
        while(second is not None):
            if(first == head):
                first.next = None
            temp = second
            second = second.next
            temp.next = first
            first = temp
        
        return first

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nodes = [1,2,3,4,5]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #1')
    print(f'solution.reverseList(head={nodes}) = {ListNode.print_linked_list_as_list(solution.reverseList(head))}')
    print(f'Expected Output: {[5,4,3,2,1]}')

    # Test Case #2
    # Inputs:
    nodes = []
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #2')
    print(f'solution.reverseList(head={nodes}) = {ListNode.print_linked_list_as_list(solution.reverseList(head))}')
    print(f'Expected Output: {[]}')

    # Test Case #2
    # Inputs:
    nodes = [1]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #3')
    print(f'solution.reverseList(head={nodes}) = {ListNode.print_linked_list_as_list(solution.reverseList(head))}')
    print(f'Expected Output: {[1]}')
