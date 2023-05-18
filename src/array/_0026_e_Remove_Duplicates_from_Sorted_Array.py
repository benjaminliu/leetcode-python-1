from typing import List


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 1
#         move = 0
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 move += 1
#             else:
#                 nums[i - move] = nums[i]
#
#         return len(nums) - move

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


Solution().removeDuplicates([1, 1])
