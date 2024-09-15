from typing import List

nums = [0,0,1,1,1,2,2,3,3,4]

nums = [1,1,2]
expectedNums = [1,2]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = set()
        for num in nums:
            result.add(num)
            
        result = sorted(result)
        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)
        
sol = Solution()
k = sol.removeDuplicates(nums)

print(k)
print(nums)
