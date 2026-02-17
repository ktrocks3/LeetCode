from typing import Optional

from common import ListNode, listToNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = head
        if not f or not f.next:
            return head
        s = head.next
        ss = s
        while (f and f.next) or (s and s.next):
            if f and f.next:
                f.next = f.next.next
                if f.next:
                    f = f.next
            if s and s.next:
                s.next = s.next.next
                s = s.next
        f.next = ss
        return head



assert Solution().oddEvenList(listToNode([1, 2, 3, 4, 5])) == [1, 3, 5, 2, 4], \
    f'Expected: [1,3,5,2,4], Received: {Solution().oddEvenList(listToNode([1, 2, 3, 4, 5]))}'
assert Solution().oddEvenList(listToNode([2, 1, 3, 5, 6, 4, 7])) == [2, 3, 6, 7, 1, 5, 4], \
    f'Expected: [2,3,6,7,1,5,4], Received: {Solution().oddEvenList(listToNode([2, 1, 3, 5, 6, 4, 7]))}'

Solution().oddEvenList(listToNode([1,2,3,4,5,6,7,8]))