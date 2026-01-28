from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(prices))]

        for i, price in enumerate(prices):
            while stack and price <= stack[-1][0]:
                x, y = stack.pop()
                result[y] = x - price
            stack.append((price, i))

        for i, j in stack:
            result[j] = i

        return result



assert Solution().finalPrices([8, 4, 6, 2, 3]) == [4,2,4,2,3], \
  f'Expected: [4,2,4,2,3], Received: {Solution().finalPrices([8, 4, 6, 2, 3])}'
assert Solution().finalPrices([1, 2, 3, 4, 5]) == [1,2,3,4,5], \
  f'Expected: [1,2,3,4,5], Received: {Solution().finalPrices([1, 2, 3, 4, 5])}'
assert Solution().finalPrices([10, 1, 1, 6]) == [9,0,1,6], \
  f'Expected: [9,0,1,6], Received: {Solution().finalPrices([10, 1, 1, 6])}'