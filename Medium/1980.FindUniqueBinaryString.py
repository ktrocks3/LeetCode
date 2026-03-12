from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l=[]
        for i in range(len(nums)):
            if nums[i][i]=='0':
                l.append('1')
            else:
                l.append('0')
        return ''.join(l)



assert Solution().findDifferentBinaryString(['1']) == "0"
assert Solution().findDifferentBinaryString(['01', '10']) == "11", \
  f'Expected: "11", Received: {Solution().findDifferentBinaryString(['01', '10'])}'
assert Solution().findDifferentBinaryString(['00', '01']) == "11", \
  f'Expected: "11", Received: {Solution().findDifferentBinaryString(['00', '01'])}'
assert Solution().findDifferentBinaryString(['111', '011', '001']) == "101", \
  f'Expected: "101", Received: {Solution().findDifferentBinaryString(['111', '011', '001'])}'