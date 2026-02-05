from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        res = []
        seen = set()
        while k > 0:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            k -= 1
            if j + 1 < len(nums2):
                if (i, j + 1) not in seen:
                    seen.add((i, j + 1))
                    heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            if i + 1 < len(nums1):
                if (i + 1, j) not in seen:
                    seen.add((i + 1, j))
                    heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        return res


assert Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]], \
    f'Expected: [[1,2],[1,4],[1,6]], Received: {Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3)}'
assert Solution().kSmallestPairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]], \
    f'Expected: [[1,1],[1,1]], Received: {Solution().kSmallestPairs([1, 1, 2], [1, 2, 3], 2)}'
