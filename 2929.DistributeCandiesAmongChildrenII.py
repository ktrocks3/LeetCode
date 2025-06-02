class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for i in range(min(limit, n)+1):
            count += max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)
        return count


assert Solution().distributeCandies(5, 2) == 3, \
    f'Expected: 3, Received: {Solution().distributeCandies(5, 2)}'
assert Solution().distributeCandies(3, 3) == 10, \
    f'Expected: 10, Received: {Solution().distributeCandies(3, 3)}'
