class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


assert Solution().strStr("sadbutsad", "sad") == 0
assert Solution().strStr("leetcode", "leeto") == -1
assert Solution().strStr("abc", "c") == 2
assert Solution().strStr("a", "a") == 0
