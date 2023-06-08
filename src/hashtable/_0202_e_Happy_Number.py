class Solution:
    def isHappy(self, n: int) -> bool:
        hset = set()
        while n != 1:
            tmp = n
            sum = 0
            while tmp > 0:
                digit = tmp % 10
                tmp = tmp // 10
                sum += digit * digit

            if sum in hset:
                return False

            hset.add(sum)
            n = sum

        return True
