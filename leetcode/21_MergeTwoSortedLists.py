# 21: Merge Two Sorted Lists

# Difficulty: Easy
# URL: https://leetcode.com/problems/merge-two-sorted-lists/
#
# Problem Description:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by 
# splicing together the list1 of the first two lists.
# Return the list1 of the merged linked list.
#
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
# - The number of list1 in both lists is in the range [0, 50].
# - -100 <= Node.val <= 100
# - Both list1 and list2 are sorted in non-decreasing order.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def build_linked_list(values: list[int]):
        if(len(values) == 0):
            return None
        list1 = ListNode(values[0])
        current = list1
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
        return list1

    def print_linked_list_as_list(list1) -> list[int]:
        current = list1
        values = []
        while(current is not None):
            values.append(current.val)
            current = current.next
        return values

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        # if both lists are empty
        if list1 is None and list2 is None:
            return None
        # only list1 is none
        if list1 is None:
            return list2
        # only list2 is none
        if list2 is None:
            return list1
        
        top = list1
        bottom = list2

        if top.val <= bottom.val:
            new_head = list1
        else:
            new_head = list2

        while top is not None and bottom is not None:
            if top.val <= bottom.val:
                # check the next one after the top
                temp = top.next
                # keep checking the next one until the top temp is greater than bottom
                while temp is not None:
                    if temp.val <= bottom.val:
                        # keep going to the next one
                        top = top.next
                        temp = temp.next
                    else:
                        break
                # top (which is 1 less than temp is now connected to bottom)
                top.next = bottom
                # new top is the temp
                top = temp
            # when top.val > bottom.val
            else:
                # same logic except we check the next one after the bottom
                temp = bottom.next
                while temp is not None:
                    if temp.val <= top.val:
                        # keep going to the next
                        bottom = bottom.next
                        temp = temp.next
                    else:
                        break
                bottom.next = top
                bottom = temp
        return new_head

if __name__ == '__main__':
    solution = Solution()

    # Test Case #1
    # Inputs:
    l1 = [1,2,3,4,5]
    list1 = ListNode.build_linked_list(l1)
    l2 = [1,3,5]
    list2 = ListNode.build_linked_list(l2)
    print('\nTest Case #1')
    print(f'solution.mergeTwoLists(list1={l1}, list2={l2}) = {ListNode.print_linked_list_as_list(solution.mergeTwoLists(list1, list2))}')
    print(f'Expected Output: {[1,1,2,3,3,4,5,5]}')

    # Test Case #2
    # Inputs:
    l1 = []
    list1 = ListNode.build_linked_list(l1)
    l2 = [1,2]
    list2 = ListNode.build_linked_list(l2)
    print('\nTest Case #2')
    print(f'solution.mergeTwoLists(list1={l1}, list2={l2}) = {ListNode.print_linked_list_as_list(solution.mergeTwoLists(list1, list2))}')
    print(f'Expected Output: {[1,2]}')

    # Test Case #3
    # Inputs:
    l1 = [-9,-7,-3,-3,-1,2,3]
    list1 = ListNode.build_linked_list(l1)
    l2 = [-7,-7,-6,-6,-5,-3,2,4]
    list2 = ListNode.build_linked_list(l2)
    print('\nTest Case #3')
    print(f'solution.mergeTwoLists(list1={l1}, list2={l2}) = {ListNode.print_linked_list_as_list(solution.mergeTwoLists(list1, list2))}')
    print(f'Expected Output: {[-9,-7,-7,-7,-6,-6,-5,-3,-3,-3,-1,2,2,3,4]}')
