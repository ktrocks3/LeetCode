class Solution:
    def twoSum(self, nums, target):
        s = {}
        for i, n in enumerate(nums):
            s[n] = i

        for i in range(len(nums)):
            j = s.get(target - nums[i])
            if j is not None and j != i:
                return [i, j]


assert Solution().twoSum([2, 7, 11, 15], 9) == [0,1], \
  f'Expected: [0,1], Received: {Solution().twoSum([2, 7, 11, 15], 9)}'
assert Solution().twoSum([3, 2, 4], 6) == [1,2], \
  f'Expected: [1,2], Received: {Solution().twoSum([3, 2, 4], 6)}'
assert Solution().twoSum([3, 3], 6) == [0,1], \
  f'Expected: [0,1], Received: {Solution().twoSum([3, 3], 6)}'