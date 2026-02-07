class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = 0         # min deletions to keep prefix balanced
        b_count = 0    # number of 'b' seen so far

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                dp = min(dp + 1, b_count)

        return dp



# assert Solution().minimumDeletions('aababbab') == 2, \
#     f'Expected: 2, Received: {Solution().minimumDeletions('aababbab')}'
assert Solution().minimumDeletions('bbaaaaabb') == 2, \
    f'Expected: 2, Received: {Solution().minimumDeletions('bbaaaaabb')}'
