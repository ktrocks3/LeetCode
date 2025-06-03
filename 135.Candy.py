from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n

        # First, give 1 candy to everyone.
        candies = [1] * n

        # 1) Left → Right pass:
        #    If ratings[i] > ratings[i-1], then i must have one more candy than i-1.
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # 2) Right → Left pass:
        #    If ratings[i] > ratings[i+1], then i must have at least candies[i+1] + 1.
        #    But we also keep whatever value it already has from the first pass.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

assert Solution().candy([1, 0, 2]) == 5, \
    f'Expected: 5, Received: {Solution().candy([1, 0, 2])}'
assert Solution().candy([1, 2, 2]) == 4, \
    f'Expected: 4, Received: {Solution().candy([1, 2, 2])}'
Solution().candy([100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60])
Solution().candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0])
Solution().candy(
    [20000, 20000, 16001, 16001, 16002, 16002, 16003, 16003, 16004, 16004, 16005, 16005, 16006, 16006, 16007, 16007,
     16008, 16008, 16009, 16009, 16010, 16010, 16011, 16011, 16012, 16012, 16013, 16013, 16014, 16014, 16015, 16015,
     16016, 16016, 16017, 16017, 16018, 16018, 16019, 16019, 16020, 16020, 16021, 16021, 16022, 16022, 16023, 16023,
     16024, 16024])
