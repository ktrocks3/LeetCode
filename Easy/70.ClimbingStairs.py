class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        res = [0] * n
        res[0] = 1
        res[1] = 2
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]


assert Solution().climbStairs(2) == 2, \
    f'Expected: 2, Received: {Solution().climbStairs(2)}'
assert Solution().climbStairs(3) == 3, \
    f'Expected: 3, Received: {Solution().climbStairs(3)}'