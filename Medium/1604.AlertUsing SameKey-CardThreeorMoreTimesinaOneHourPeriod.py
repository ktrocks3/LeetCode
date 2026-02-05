from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic = defaultdict(list)
        for i, name in enumerate(keyName):
            dic[name].append(int(keyTime[i].replace(":", "")))
        ans = []
        for n, m in dic.items():
            m.sort()
            l = len(m)
            for h in range(l - 2):
                if m[h + 2] - m[h] <= 100:
                    ans.append(n)
                    break
        return sorted(ans)


assert Solution().alertNames(["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
                             ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]) == ['daniel']
assert Solution().alertNames(["a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c"],
                             ["01:35", "08:43", "20:49", "00:01", "17:44", "02:50", "18:48", "22:27", "14:12", "18:00",
                              "12:38", "20:40", "03:59", "22:24"]) == []

assert Solution().alertNames(["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b"],
                             ["23:27", "03:14", "12:57", "13:35", "13:18", "21:58", "22:39", "10:49", "19:37", "14:14",
                              "10:41"]) == ['a']
