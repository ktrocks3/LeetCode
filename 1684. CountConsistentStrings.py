from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            flag = True
            for w in word:
                if w not in allowed:
                    flag = False
                    break
            if flag:
                count += 1
        return count


assert Solution().countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]) == 2
assert Solution().countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7
assert Solution().countConsistentStrings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == 4
