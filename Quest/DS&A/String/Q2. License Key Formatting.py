class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        first = len(s) % k
        res = []
        if first:
            res.append(s[:first])
        while first < len(s):
            res.append(s[first:first+k])
            first += k
        return '-'.join(res)


assert Solution().licenseKeyFormatting('5F3Z-2e-9-w', 4) == "5F3Z-2E9W", \
  f'Expected: "5F3Z-2E9W", Received: {Solution().licenseKeyFormatting('5F3Z-2e-9-w', 4)}'
assert Solution().licenseKeyFormatting('2-5g-3-J', 2) == "2-5G-3J", \
  f'Expected: "2-5G-3J", Received: {Solution().licenseKeyFormatting('2-5g-3-J', 2)}'