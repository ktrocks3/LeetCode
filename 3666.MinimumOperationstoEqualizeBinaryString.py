import collections
from math import inf


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        def make_dsu(m):
            parent = list(range(m + 1))  # m is sentinel (means "none left")

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def erase(x):
                parent[x] = find(x + 1)

            return find, erase

        n = len(s)
        z = len([x for x in s if x == '0'])
        # So there's z 0s and n-z 1s, we have to choose k indices, so if I let i = #0s chosen then
        # z' = z - i + (k - i) = z + k - 2i. So we have to choose what values of i are possible:
        # i <= z since you can't pick more 0s than exist. k-i <= n so i >= k - (n - z)
        # So max(0, k-(n-z)) <= i <= min(k,z) so smallest z' = z + k - 2i_max, largest z' = z + k - 2 i_min.
        bfs, dist = collections.deque([z]), [-1] * (n + 1)
        dist[z] = 0
        m0 = (n - 0) // 2 + 1
        m1 = (n - 1) // 2 + 1
        f0, e0 = make_dsu(m0)
        f1, e1 = make_dsu(m1)
        find = [f0, f1]
        erase = [e0, e1]
        erase[z % 2]((z - (z % 2)) // 2)

        while bfs:
            z = bfs.popleft()
            if z == 0:
                return dist[0]
            iMax = min(k, z)
            iMin = max(0, k - (n - z))
            p = (z + k) % 2

            smallest = z + k - 2 * iMax
            largest = z + k - 2 * iMin
            smallest = max(smallest, 0)
            largest = min(largest, n)
            smallest = smallest if smallest % 2 == p else smallest + 1
            largest = largest if largest % 2 == p else largest - 1
            if smallest > largest:
                continue

            smallest = (smallest - p) // 2
            largest = (largest - p) // 2
            i = find[p](smallest)
            while i <= largest:
                dist[2 * i + p] = dist[z] + 1
                bfs.append(2 * i + p)
                erase[p](i)
                i = find[p](i)

        return -1


class Solution2:
    def minOperations(self, s: str, k: int) -> int:

        n = len(s)
        z = s.count('0')

        if n == k:
            if z == 0:
                return 0
            elif z == n:
                return 1
            else:
                return -1

        def ceil(x, y):
            return (x + y - 1) // y

        ans = inf

        if z % 2 == 0:
            m = max(ceil(z, k), ceil(z, n - k))
            if m % 2 == 1:
                m += 1
            ans = min(ans, m)

        if z % 2 == k % 2:
            m = max(ceil(z, k), ceil(n - z, n - k))
            if m % 2 == 0:
                m += 1
            ans = min(ans, m)

        return ans if ans < inf else -1


S = Solution2()
assert S.minOperations('110', 1) == 1, \
    f'Expected: 1, Received: {S.minOperations('110', 1)}'
assert S.minOperations('0101', 3) == 2, \
    f'Expected: 2, Received: {S.minOperations('0101', 3)}'
assert S.minOperations('101', 2) == -1, \
    f'Expected: -1, Received: {S.minOperations('101', 2)}'
