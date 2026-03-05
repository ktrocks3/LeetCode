class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        running = 1
        prev = 0
        ans = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(prev, running)
                prev = running
                running = 1
            else:
                running += 1
        ans += min(prev, running)
        return ans


assert Solution().countBinarySubstrings('00110011') == 6, \
    f'Expected: 6, Received: {Solution().countBinarySubstrings('00110011')}'
assert Solution().countBinarySubstrings('10101') == 4, \
    f'Expected: 4, Received: {Solution().countBinarySubstrings('10101')}'
