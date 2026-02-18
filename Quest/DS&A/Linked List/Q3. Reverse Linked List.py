from typing import Optional

from common import ListNode, listToNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        if not current:
            return head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev



assert Solution().reverseList(listToNode([1, 2, 3, 4, 5])) == [5,4,3,2,1], \
  f'Expected: [5,4,3,2,1], Received: {Solution().reverseList(listToNode([1, 2, 3, 4, 5]))}'
assert Solution().reverseList(listToNode([1, 2])) == [2,1], \
  f'Expected: [2,1], Received: {Solution().reverseList(listToNode([1, 2]))}'
assert Solution().reverseList(listToNode([])) == listToNode([]), \
  f'Expected: [], Received: {Solution().reverseList(listToNode([]))}'