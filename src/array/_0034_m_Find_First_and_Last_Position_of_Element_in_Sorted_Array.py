class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[0] > target or nums[len(nums) - 1] < target:
            return [-1, -1]

        first = self.findFirst(nums, target)
        if first == -1:
            return [-1, -1]

        last = self.findLast(nums, target)
        return [first, last]

    def findFirst(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                if mid == 0:
                    return 0;
                if nums[mid - 1] != target:
                    return mid

                hi = mid - 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

    def findLast(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        last = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                if mid == last:
                    return last

                if nums[mid + 1] != target:
                    return mid

                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1
