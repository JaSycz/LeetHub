class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maxtotal = total
        
        for i in range(len(nums)-k):
            total += nums[i+k]
            total -= nums[i]
            maxtotal = max(maxtotal,total)
        
        return maxtotal/k