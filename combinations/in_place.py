"""
https://leetcode.com/problems/combinations/description/
"""
from typing import List


class Solution:
    def getCombinations(
        self,
        result: List[List[int]],
        k: int,
        input_array: List[int],
        cur_pos: int,
        swap_start_pos: int,
    ):
        if k == 0:
            result.append(input_array[0 : self.K])
            return

        self.getCombinations(result, k - 1, input_array, cur_pos + 1, swap_start_pos)

        for i in range(swap_start_pos, len(input_array)):
            input_array[cur_pos], input_array[i] = input_array[i], input_array[cur_pos]
            self.getCombinations(result, k - 1, input_array, cur_pos + 1, i + 1)
            input_array[cur_pos], input_array[i] = input_array[i], input_array[cur_pos]

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        input_array = [i for i in range(1, n + 1)]
        self.K = k

        self.getCombinations(result, k, input_array, 0, k)

        return result


print(Solution().combine(5, 3))
