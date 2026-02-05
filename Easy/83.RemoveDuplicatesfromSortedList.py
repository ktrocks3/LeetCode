# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        og = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return og


l = ListNode(1, ListNode(1, ListNode(2, None)))
l = Solution().deleteDuplicates(l)
a = []
while l:
    a.append(l.val)
    l = l.next
assert a == [1, 2]

l = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))
l = Solution().deleteDuplicates(l)
a = []
while l:
    a.append(l.val)
    l = l.next
assert a == [1, 2, 3]
