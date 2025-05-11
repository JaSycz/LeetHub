from collections import defaultdict

class Solution:
    
    
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        val = -1

        for i in nums:
            if count == 0:
                val = i
                count=1
            else:
                if i == val:
                    count+=1
                else:
                    count-=1

        return val
