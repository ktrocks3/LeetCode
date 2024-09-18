class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = bin(start)
        y = bin(goal)
        while len(x) != len(y):
            if len(x) < len(y):
                x = x[:2] + '0' + x[2:]
            else:
                y = y[:2] + '0' + y[2:]
        res = 0
        for i in range(2, len(x)):
            if x[i] != y[i]:
                res += 1
        return res


assert Solution().minBitFlips(10, 7) == 3
assert Solution().minBitFlips(3, 4) == 3
assert Solution().minBitFlips(10, 82) == 3
