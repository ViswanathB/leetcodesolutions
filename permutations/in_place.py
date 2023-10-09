"""
https://leetcode.com/problems/permutations/description/
"""
from typing import List


class Solution:
    def getPermutation(self, nums: List[int], result: List[List[int]], k: int, cur_pos: int):
        if k == len(nums):
            result.append(nums[:])
            return

        self.getPermutation(nums, result, k + 1, cur_pos + 1)

        for i in range(cur_pos + 1, len(nums)):
            nums[cur_pos], nums[i] = nums[i], nums[cur_pos]
            self.getPermutation(nums, result, k + 1, cur_pos + 1)
            nums[cur_pos], nums[i] = nums[i], nums[cur_pos]

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.getPermutation(nums, result, 1, 0)

        return result


print(Solution().permute([1, 2, 3, 4]))
