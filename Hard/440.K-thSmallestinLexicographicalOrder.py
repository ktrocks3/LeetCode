class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def calc_steps(curr, n):
            steps = 0
            nxt = curr + 1
            while curr <= n:
                steps += min(n + 1, nxt) - curr
                curr *= 10
                nxt *= 10
            return steps

        curr = 1
        k -= 1

        while k > 0:
            steps = calc_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1

        return curr


assert Solution().findKthNumber(13, 2) == 10
assert Solution().findKthNumber(1, 1) == 1
