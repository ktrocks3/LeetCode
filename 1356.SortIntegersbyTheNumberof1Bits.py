from itertools import count
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x: (x.bit_count(), x))


assert Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0,1,2,4,8,3,5,6,7], \
  f'Expected: [0,1,2,4,8,3,5,6,7], Received: {Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8])}'
assert Solution().sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [1,2,4,8,16,32,64,128,256,512,1024], \
  f'Expected: [1,2,4,8,16,32,64,128,256,512,1024], Received: {Solution().sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])}'