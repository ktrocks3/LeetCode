from itertools import permutations, combinations
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        leds = [
            (8, "h"), (4, "h"), (2, "h"), (1, "h"),  # Hour LEDs
            (32, "m"), (16, "m"), (8, "m"), (4, "m"), (2, "m"), (1, "m")  # Min LEDs
        ]

        res = []

        for selection in combinations(leds, turnedOn):
            h_sum = 0
            m_sum = 0

            for value, unit in selection:
                if unit == "h":
                    h_sum += value
                else:
                    m_sum += value

            if h_sum < 12 and m_sum < 60:
                res.append(f"{h_sum}:{m_sum:02d}")

        return res


assert sorted(Solution().readBinaryWatch(1)) == ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00",
                                         "8:00"], \
    f'Expected: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"], Received: {Solution().readBinaryWatch(1)}'
assert Solution().readBinaryWatch(9) == [], \
    f'Expected: [], Received: {Solution().readBinaryWatch(9)}'
