"""
https://leetcode.com/problems/permutations-ii/
"""
from typing import List


class Solution:
    def getPermutation(self, nums: List[int], result: List[List[int]], k: int, cur_pos: int):
        if k == len(nums):
            result.append(nums[:])
            return

        self.getPermutation(nums, result, k + 1, cur_pos + 1)

        prev_item = set()
        prev_item.add(nums[cur_pos])

        i = cur_pos + 1
        while i < len(nums):
            if nums[i] in prev_item:
                i += 1
                continue

            prev_item.add(nums[i])

            nums[cur_pos], nums[i] = nums[i], nums[cur_pos]
            self.getPermutation(nums, result, k + 1, cur_pos + 1)
            nums[cur_pos], nums[i] = nums[i], nums[cur_pos]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        self.getPermutation(nums, result, 1, 0)

        return result


result = Solution().permuteUnique([0, 0, 0, 1, 1, 9, 9])
print(f"Total permutations: {len(result)}")
print(result)
