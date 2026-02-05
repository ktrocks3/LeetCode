from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                right = i - 1
                area = max(area, (right - left + 1) * height)

            stack.append(i)
        return area


assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, \
    f'Expected: 10, Received: {Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])}'
assert Solution().largestRectangleArea([2, 4]) == 4, \
    f'Expected: 4, Received: {Solution().largestRectangleArea([2, 4])}'
