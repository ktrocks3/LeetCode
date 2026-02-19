"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional, List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        return f"({self.val}, {self.next.val if self.next else None}, {self.random.val if self.random else None})"


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldnew = {None: None}
        point = head
        while point:
            oldnew[point] = Node(point.val)
            point = point.next

        point = head
        while point:
            current_point, next_point, random_point = oldnew[point], oldnew[point.next], oldnew[point.random]
            current_point.next = next_point
            current_point.random = random_point
            point = point.next

        return oldnew[head]

class Solution2:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            copy = Node(cur.val, cur.next)
            cur.next = copy
            cur = copy.next

        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur = head
        new_head = head.next
        while cur:
            copy = cur.next
            cur.next = copy.next
            copy.next = copy.next.next if copy.next else None
            cur = cur.next

        return new_head
