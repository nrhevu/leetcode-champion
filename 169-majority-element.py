from random import randint
from typing import List

nums = [2,2,1,1,1,2,2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        current = nums[0]
        count = 1

        max_count = count
        max_count_num = current
        
        for i in range(1, len(nums)):
            if nums[i] == current:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                    max_count_num = current
                current = nums[i]
                count = 1
        
        if count > max_count:
            max_count = count
            max_count_num = current        
        
        return max_count_num
    
sol = Solution()
k = sol.majorityElement(nums)

print(k)
