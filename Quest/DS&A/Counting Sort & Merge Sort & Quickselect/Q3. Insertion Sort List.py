# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from common import ListNode, listToNode


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sorted_list = head
        curr = head.next
        sorted_list.next = None
        while curr:
            next_node = curr.next

            if curr.val < sorted_list.val:
                curr.next = sorted_list
                sorted_list = curr

            else:
                prev = sorted_list
                while prev.next and prev.next.val < curr.val:
                    prev = prev.next

                curr.next = prev.next
                prev.next = curr


            curr = next_node

        return sorted_list

        return None


assert Solution().insertionSortList(listToNode([4, 2, 1, 3])) == listToNode([1, 2, 3, 4]), \
    f'Expected: listToNode([1,2,3,4]), Received: {Solution().insertionSortList(listToNode([4, 2, 1, 3]))}'
assert Solution().insertionSortList(listToNode([-1, 5, 3, 4, 0])) == listToNode([-1, 0, 3, 4, 5]), \
    f'Expected: listToNode([-1,0,3,4,5]), Received: {Solution().insertionSortList(listToNode([-1, 5, 3, 4, 0]))}'
