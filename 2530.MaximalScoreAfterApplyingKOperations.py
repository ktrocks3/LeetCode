"""
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = []
        score = 0
        for num in nums:
            heappush(h, -1 * num)
        for i in range(k):
            val = heappop(h)
            score += val
            heappush(h, val // 3)
        return score * -1


assert Solution().maxKelements([10, 10, 10, 10, 10], 6) == 54
assert Solution().maxKelements([1, 10, 3, 3, 3], 3) == 17
