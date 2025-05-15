from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        next_check = -1
        for i, group in enumerate(groups):
            if group != next_check:
                next_check = group
                res.append(words[i])
        return res



assert Solution().getLongestSubsequence(['e', 'a', 'b'], [0, 0, 1]) == ["e","b"], \
  f'Expected: ["e","b"], Received: {Solution().getLongestSubsequence(['e', 'a', 'b'], [0, 0, 1])}'
assert Solution().getLongestSubsequence(['a', 'b', 'c', 'd'], [1, 0, 1, 1]) == ["a","b","c"], \
  f'Expected: ["a","b","c"], Received: {Solution().getLongestSubsequence(['a', 'b', 'c', 'd'], [1, 0, 1, 1])}'