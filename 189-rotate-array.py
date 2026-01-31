from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k %len(nums)
        
        inplace_array = nums[-k:] + nums[:-k]
        
        for i in range(len(nums)):
            nums[i] = inplace_array[i]
