class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]  # Reverse the string
        n = len(s)

        # Find the longest palindrome prefix
        for i in range(n):
            if s[:n - i] == rev_s[i:]:
                # Append the non-matching part of the reversed string to the front
                return rev_s[:i] + s
        return ""
# Test cases
assert Solution().shortestPalindrome("aacecaaa") == "aaacecaaa"
assert Solution().shortestPalindrome("abcd") == "dcbabcd"
assert Solution().shortestPalindrome("") == ""
