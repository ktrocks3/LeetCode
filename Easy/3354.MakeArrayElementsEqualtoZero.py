from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def scan(start, direction):
            n = len(nums)
            curr = start
            while 0 <= curr < n:
                if nums[curr] == 0:
                    curr += direction
                elif nums[curr] > 0:
                    nums[curr] -= 1
                    direction = -direction
                    curr += direction
                else:
                    break

        zeros = [i for i, x in enumerate(nums) if x == 0]
        original_nums = nums[:]
        valid_count = 0

        for zero in zeros:
            nums = original_nums[:]
            scan(zero, 1)  # Right direction
            if all(x == 0 for x in nums):
                valid_count += 1

            nums = original_nums[:]
            scan(zero, -1)  # Left direction
            if all(x == 0 for x in nums):
                valid_count += 1

        return valid_count


assert Solution().countValidSelections([1, 0, 2, 0, 3]) == 2
