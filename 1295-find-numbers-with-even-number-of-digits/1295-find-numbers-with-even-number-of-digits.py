class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count,res = 0,0

        for n in nums:
            for c in str(n):
                count+=1
            if count%2==0:
                res+=1
            count=0
        
        return res