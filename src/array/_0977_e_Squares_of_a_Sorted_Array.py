class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lo, hi = 0, len(nums) - 1
        idx = hi

        res = [0] * len(nums)
        while lo < hi:
            l = nums[lo] * nums[lo]
            r = nums[hi] * nums[hi]

            if l > r:
                lo += 1
                res[idx] = l
            else:
                hi -= 1
                res[idx] = r

            idx -= 1

        res[0] = nums[lo] * nums[lo]
        return res
