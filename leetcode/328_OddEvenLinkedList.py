# 328. Odd Even Linked List

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]

# Accepted 1.1M
# Submissions 1.9M
# Acceptance Rate 61.8%


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

    def print_linked_list_as_list(head) -> list[int]:
        current = head
        values = []
        while(current is not None):
            values.append(current.val)
            current = current.next
        return values

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total_head = 0
        node = head
        # count the number of head
        while(node is not None):
            total_head += 1
            node = node.next
        
        # edge cases
        # Number of linked list head is 0, 1 or 2
        if(total_head < 3):
            return head
        
        odd_index = head
        even_index = head.next
        even_start_index = head.next
        while(odd_index and even_index):
            if(even_index.next is not None):
                odd_index.next = even_index.next
                odd_index = even_index.next
            else:
                break
            even_index.next = odd_index.next
            even_index = odd_index.next
        # loop is done now setting the last odd index to start
        # from the first even index
        odd_index.next = even_start_index
        # if the last even index is not set to None, we set it to None
        if(even_index is not None):
            even_index.next = None
        return head
    
if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    nodes = [1,2,3,4,5]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #1')
    print(f'solution.oddEvenList(head={nodes}) = {ListNode.print_linked_list_as_list(solution.oddEvenList(head))}')
    print(f'Expected Output: {[1,3,5,2,4]}')

    # Test Case #2
    # Inputs:
    nodes = [2,1,3,5,6,4,7]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #2')
    print(f'solution.oddEvenList(head={nodes}) = {ListNode.print_linked_list_as_list(solution.oddEvenList(head))}')
    print(f'Expected Output: {[2,3,6,7,1,5,4]}')

    # Test Case #3
    # Inputs:
    nodes = []
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #3')
    print(f'solution.oddEvenList(head={nodes}) = {ListNode.print_linked_list_as_list(solution.oddEvenList(head))}')
    print(f'Expected Output: {[]}')

    # Test Case #4
    # Inputs:
    nodes = [1]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #4')
    print(f'solution.oddEvenList(head={nodes}) = {ListNode.print_linked_list_as_list(solution.oddEvenList(head))}')
    print(f'Expected Output: {[1]}')

    # Test Case #5
    # Inputs:
    nodes = [1,2]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #5')
    print(f'solution.oddEvenList(head={nodes}) = {ListNode.print_linked_list_as_list(solution.oddEvenList(head))}')
    print(f'Expected Output: {[1,2]}')

    # Test Case #6
    # Inputs:
    nodes = [2,1,3,5,6,4]
    head = ListNode.build_linked_list(nodes)
    print('\nTest Case #6')
    print(f'solution.oddEvenList(head={nodes}) = {ListNode.print_linked_list_as_list(solution.oddEvenList(head))}')
    print(f'Expected Output: {[2,3,6,1,5,4]}')