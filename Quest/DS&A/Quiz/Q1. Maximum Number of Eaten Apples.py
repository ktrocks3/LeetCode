import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap, n, day, eaten = [], len(apples), 0, 0
        while day < n or heap:
            if day < n and apples[day] >= 0:
                heapq.heappush(heap, (day + days[day], apples[day]))

            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            if heap:
                expire, count = heapq.heappop(heap)
                eaten += 1
                if count > 1:
                    heapq.heappush(heap, (expire, count - 1))
            day += 1
        return eaten


# print(Solution().eatenApples([1,2,3,5,2], [3,2,1,4,2]))
# print(Solution().eatenApples([3,0,0,0,0,2], [3,0,0,0,0,2]))
print(Solution().eatenApples([2, 1, 1, 4, 5], [10, 10, 6, 4, 2]))
