class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 0, num

        while lo <= hi:
            mid = (lo + hi)//2
            sqr = mid * mid
            if sqr == num:
                return True

            if sqr > num:
                hi = mid -1
            else:
                lo = mid + 1

        return False