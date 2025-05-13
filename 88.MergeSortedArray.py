from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lp, rp = m-1, n-1
        for i in range(len(nums1)-1, -1, -1):
            if lp < 0 or (rp >= 0 and nums2[rp] > nums1[lp]):
                nums1[i] = nums2[rp]
                rp -= 1
            else:
                nums1[i] = nums1[lp]
                lp -= 1



nums1 = [2]
Solution().merge(nums1, m = 1, nums2 = [], n = 0)
print(nums1)