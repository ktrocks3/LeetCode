from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices


assert Solution().finalPrices([8, 4, 6, 2, 3]) == [4,2,4,2,3], \
  f'Expected: [4,2,4,2,3], Received: {Solution().finalPrices([8, 4, 6, 2, 3])}'
assert Solution().finalPrices([1, 2, 3, 4, 5]) == [1,2,3,4,5], \
  f'Expected: [1,2,3,4,5], Received: {Solution().finalPrices([1, 2, 3, 4, 5])}'
assert Solution().finalPrices([10, 1, 1, 6]) == [9,0,1,6], \
  f'Expected: [9,0,1,6], Received: {Solution().finalPrices([10, 1, 1, 6])}'