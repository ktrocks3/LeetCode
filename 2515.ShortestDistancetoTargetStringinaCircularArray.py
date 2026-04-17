from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        left = 1
        n = len(words)
        current = (startIndex + 1) % n
        while current != startIndex:
            if words[current] == target:
                break
            left += 1
            current = (current + 1) % n
        if current == startIndex:
            return -1

        right = 1
        current = (startIndex - 1) % n
        while current != startIndex:
            if words[current] == target:
                break
            right += 1
            current = (current - 1) % n

        if current == startIndex:
            return -1

        return min(left, right)


assert Solution().closestTarget(['hello', 'i', 'am', 'leetcode', 'hello'], 'hello', 1) == 1, \
  f'Expected: 1, Received: {Solution().closestTarget(['hello', 'i', 'am', 'leetcode', 'hello'], 'hello', 1)}'
assert Solution().closestTarget(['a', 'b', 'leetcode'], 'leetcode', 0) == 1, \
  f'Expected: 1, Received: {Solution().closestTarget(['a', 'b', 'leetcode'], 'leetcode', 0)}'
assert Solution().closestTarget(['i', 'eat', 'leetcode'], 'ate', 0) == -1, \
  f'Expected: -1, Received: {Solution().closestTarget(['i', 'eat', 'leetcode'], 'ate', 0)}'
