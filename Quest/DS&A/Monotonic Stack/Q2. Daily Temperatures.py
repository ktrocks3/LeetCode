from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                x = stack.pop()
                result[x] = i - x
            stack.append(i)
        return result

assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1,1,4,2,1,1,0,0], \
  f'Expected: [1,1,4,2,1,1,0,0], Received: {Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])}'
assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1,1,1,0], \
  f'Expected: [1,1,1,0], Received: {Solution().dailyTemperatures([30, 40, 50, 60])}'
assert Solution().dailyTemperatures([30, 60, 90]) == [1,1,0], \
  f'Expected: [1,1,0], Received: {Solution().dailyTemperatures([30, 60, 90])}'
