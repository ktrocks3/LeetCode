class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        def swap(arr, i, j):
            arr = arr.copy()
            arr[i], arr[j] = arr[j], arr[i]
            return str(arr)
        s1Options = {str(s1), swap(s1, 0, 2), swap(s1, 1, 3)}
        s2Options = {str(s2), swap(s2, 0, 2), swap(s2, 1, 3)}
        return len(s1Options.intersection(s2Options)) > 0


assert Solution().canBeEqual('abcd', 'cdab') == True, \
  f'Expected: True, Received: {Solution().canBeEqual('abcd', 'cdab')}'
assert Solution().canBeEqual('abcd', 'dacb') == False, \
  f'Expected: False, Received: {Solution().canBeEqual('abcd', 'dacb')}'
