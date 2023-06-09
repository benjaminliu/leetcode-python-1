class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hmap = dict()
        for i in nums1:
            for j in nums2:
                sum = i + j
                if sum in hmap:
                    hmap[sum] += 1
                else:
                    hmap[sum] = 1

        res = 0
        for i in nums3:
            for j in nums4:
                rest = 0 - i - j
                if rest in hmap:
                    res += hmap[rest]

        return res