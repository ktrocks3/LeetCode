class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = s.count('1')
        ans = 0
        for i in range(len(s)-1):
            left += 1 if s[i]=='0' else 0
            right += 0 if s[i]=='0' else -1
            ans = max(left+right,ans)
        return ans


assert Solution().maxScore('011101') == 5, \
    f'Expected: 5, Received: {Solution().maxScore('011101')}'
assert Solution().maxScore('00111') == 5, \
    f'Expected: 5, Received: {Solution().maxScore('00111')}'
assert Solution().maxScore('00') == 1, \
    f'Expected: 1, Received: {Solution().maxScore('00')}'
