class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        start,end,count = 0,2,0

        while end < len(nums):
            if (nums[start]+nums[end])*2 == nums[(start+end)//2]:
                count+= 1 
            start+= 1
            end+=1
            
        return count