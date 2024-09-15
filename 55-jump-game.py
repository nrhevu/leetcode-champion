from typing import List

nums = [2,3,1,1,4]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fartest = 0
        
        for i in range(len(nums) - 1):
            if i > fartest:
                break
            fartest = max(fartest, i + nums[i])
                    
        return True if fartest >= len(nums) - 1 else False
    
sol = Solution()

print(sol.canJump(nums))