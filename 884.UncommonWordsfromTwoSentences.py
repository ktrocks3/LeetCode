from typing import List, Set, Any


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> set[Any]:
        # Essentially it being two sentences doesn't matter, it's the same as if it's one.
        seen = set()
        common = set()
        s1 = s1.split()
        for word in s1: # O(n)
            if word in seen:
                common.add(word)
            else:
                seen.add(word)
        s2 = s2.split()
        for word in s2: # O(n)
            if word in seen:
                common.add(word)
            else:
                seen.add(word)

        return seen.difference(common) # O(n)

assert Solution().uncommonFromSentences("this apple is sweet", "this apple is sour") == {'sour', 'sweet'}
assert Solution().uncommonFromSentences("apple apple", "banana") == {"banana"}
