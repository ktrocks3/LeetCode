from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for point in timePoints:  # O(n)
            h, m = point.split(":")
            h, m = int(h), int(m)
            minutes.append(m + h * 60)

        minutes = sorted(minutes)  # O(n log n)
        min_diff = 1441
        # Find minimum difference between consecutive times
        for i in range(1, len(minutes)):  # O(n)
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # Check the difference between the last and first time considering wrap-around
        min_diff = min(min_diff, (1440 - minutes[-1] + minutes[0]))

        return min_diff  # 2 * O(n) + O(n log n) = O(n log n)


assert Solution().findMinDifference(["23:59", "00:00"]) == 1
assert Solution().findMinDifference(["00:00", "23:59"]) == 1
assert Solution().findMinDifference(["00:00", "04:00", "22:00"]) == 120
assert Solution().findMinDifference(["00:00", "23:59", "00:00"]) == 0
assert Solution().findMinDifference(["12:12", "00:13"]) == 719
