from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Create a prefix sum array
        prefix_sum = [0]
        for w in words:
            is_vowel_string = 1 if w[0] in vowels and w[-1] in vowels else 0
            prefix_sum.append(prefix_sum[-1] + is_vowel_string)

        # Resolve queries using the prefix sum array
        res = []
        for l, r in queries:
            res.append(prefix_sum[r + 1] - prefix_sum[l])

        return res
