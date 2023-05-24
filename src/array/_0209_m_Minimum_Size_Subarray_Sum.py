from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        minLen = len(nums) + 1

        for right in range(0, len(nums)):
            sum += nums[right]
            while sum >= target:
                temp = right - left + 1
                minLen = temp if temp < minLen else minLen
                sum -= nums[left]
                left += 1

        return 0 if minLen > len(nums) else minLen


Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
