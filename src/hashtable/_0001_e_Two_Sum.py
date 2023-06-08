from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            num1 = nums[i]
            remain = target - num1
            if remain in hmap:
                return [i, hmap[remain]]

            hmap[num1] = i

        return None
