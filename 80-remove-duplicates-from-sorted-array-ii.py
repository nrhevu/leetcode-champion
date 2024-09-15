from typing import List

nums = [1,1,1,2,2,3]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        
        current = nums[0]
        count = 1
        
        i = 1
        while i < len(nums):
            if nums[i] == current:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                current = nums[i]
                count = 1
            i += 1
        return len(nums)
    
sol = Solution()
k = sol.removeDuplicates(nums)

print(k)
print(nums)