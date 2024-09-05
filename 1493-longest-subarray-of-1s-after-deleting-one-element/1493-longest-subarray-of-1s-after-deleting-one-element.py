class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start,end = 0,0
        count_zero = 0

        while end < len(nums):
            if nums[end] == 0:
                count_zero += 1
            if count_zero > 1:
                if nums[start] == 0:
                    count_zero -=1
                start+= 1
            
            end+=1
        
        return end-start-1