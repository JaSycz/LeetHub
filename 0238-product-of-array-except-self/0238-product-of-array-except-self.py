class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lst = [1] * len(nums)
        
        
        products_left = 1
        for i in range(len(nums)):
            lst[i]*= products_left
            products_left*= nums[i]
        
        products_right = 1
        for i in range(len(nums) - 1,-1,-1):
            lst[i] *= products_right
            products_right *= nums[i]
            
        return lst
        
        
        
            