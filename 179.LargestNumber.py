from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings
        nums = list(map(str, nums)) #O(n)

        # Sort numbers based on which concatenation is larger: x + y or y + x
        # 330 > 303 but '3' < '30' but '3'*10 > '30'*10 so we sort on val*10
        nums.sort(key=lambda x: x * 2, reverse=True) #O(n log n)

        # Join the sorted numbers into the largest possible number
        result = ''.join(nums) #O(n)

        # Handle the case where the result is all zeros (e.g., [0, 0])
        if result[0] == '0': #O(1)
            return '0'

        return result #O(n log n)


assert Solution().largestNumber([10, 2]) == '210'
assert Solution().largestNumber([3, 30, 34, 5, 9]) == '9534330'
assert Solution().largestNumber([0, 0]) == '0'
assert Solution().largestNumber([74, 21, 33, 51, 77, 51, 90, 60, 5, 56]) == '9077746056551513321'
