from typing import Optional

from common import ListNode, listToNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        og = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return og


assert Solution().deleteDuplicates(listToNode([1, 1, 2])) == [1, 2], \
    f'Expected: [1,2], Received: {Solution().deleteDuplicates(listToNode([1, 1, 2]))}'
assert Solution().deleteDuplicates(listToNode([1, 1, 2, 3, 3])) == [1, 2, 3], \
    f'Expected: [1,2,3], Received: {Solution().deleteDuplicates(listToNode([1, 1, 2, 3, 3]))}'
