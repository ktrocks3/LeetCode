from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        best, j, n = 0, 0, len(nums)
        for i in range(n):
            if j < i:
                j = i
            while j < n and k * nums[i] >= nums[j]:
                j += 1
            best = max(best, j - i)
        return n - best


assert Solution().minRemoval([2, 1, 5], 2) == 1, \
    f'Expected: 1, Received: {Solution().minRemoval([2, 1, 5], 2)}'
assert Solution().minRemoval([1, 6, 2, 9], 3) == 2, \
    f'Expected: 2, Received: {Solution().minRemoval([1, 6, 2, 9], 3)}'
assert Solution().minRemoval([4, 6], 2) == 0, \
    f'Expected: 0, Received: {Solution().minRemoval([4, 6], 2)}'
assert Solution().minRemoval([2, 12], 2) == 1, \
    f'Expected: 0, Received: {Solution().minRemoval([2, 12], 2)}'
assert Solution().minRemoval([8], 1) == 0, \
    f'Expected: 0, Received: {Solution().minRemoval([8], 1)}'

Solution().minRemoval([2, 1, 5], 2)
Solution().minRemoval([2, 12], 2)
Solution().minRemoval([8], 1)
Solution().minRemoval([32, 607, 740, 134, 944, 91, 410, 155, 493, 89, 12], 10)
Solution().minRemoval([1, 34, 23], 2)
Solution().minRemoval(
    [26155, 1776, 22815, 775, 27772, 12869, 12995, 22794, 27692, 24728, 10944, 25039, 24068, 25506, 18506, 19138, 12331,
     17814, 20834, 21474, 20208, 21590, 15453, 6114, 25716, 29434, 23547, 29051, 25992, 5535, 7387], 80020)
Solution().minRemoval(
    [9514, 4037, 4183, 20670, 24972, 13008, 31534, 34223, 22722, 7793, 15527, 37410, 28870, 7506, 3485, 19748, 26934,
     333, 38955, 831, 6658, 24063, 10075, 14595, 15246, 5715, 3382, 27295, 6093, 24611, 14191, 31204, 14631, 12630], 1)
