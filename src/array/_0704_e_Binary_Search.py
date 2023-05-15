from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1


print(Solution().search([-1,0,3,5,9,12],9))