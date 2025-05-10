class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0
        count = 0

        while i<=j:
            if nums[j] == val:
                nums[j] = '_'
                j-=1
                count+=1
                continue

            if nums[i] == val:
                nums[i] = nums[j]
                nums[j] = '_'
                j-=1
                count+=1
            i+=1
        
        
        k = len(nums) - count

        return k
                 
