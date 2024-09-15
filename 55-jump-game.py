from typing import List

nums = [2,3,1,1,4]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [0] * len(nums)
        reachable[0] = 1
        
        for i in range(len(nums)):
            if reachable[i]:
                for j in range(i + 1, min(len(nums), nums[i] + i + 1)):
                    reachable[j] = 1
                    
        return True if reachable[-1] == 1 else False
    
sol = Solution()

print(sol.canJump(nums))