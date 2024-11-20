class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0
        ans = n
        a, b, c = 0, 0, 0

        # Count total occurrences of 'a', 'b', and 'c'
        totalA, totalB, totalC = s.count('a'), s.count('b'), s.count('c')

        # If there are not enough 'a', 'b', or 'c', return -1
        if totalA < k or totalB < k or totalC < k:
            return -1

        # Reset counters and start sliding window
        while r < n:
            if s[r] == 'a': a += 1
            if s[r] == 'b': b += 1
            if s[r] == 'c': c += 1
            r += 1

            # Shrink window if it exceeds the limits
            while a > totalA - k or b > totalB - k or c > totalC - k:
                if s[l] == 'a': a -= 1
                if s[l] == 'b': b -= 1
                if s[l] == 'c': c -= 1
                l += 1

            # Update the answer with the minimum number of characters to remove
            ans = min(ans, n - (r - l))

        return ans


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.takeCharacters("aabaaaacaabc", 2) == 8, "Test Case 1 Failed"
    assert solution.takeCharacters("a", 1) == -1, "Test Case 2 Failed"
    print("All test cases passed!")
