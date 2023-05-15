class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        if nums[lo] > target:
            return 0

        if nums[hi] < target:
            return len(nums)

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
