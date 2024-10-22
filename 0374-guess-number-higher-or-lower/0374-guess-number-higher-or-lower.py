# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        nums = [num for num in range(1,n+1)]
        print(nums)
        i,j = 0,len(nums)-1
        mid = len(nums)//2
        while guess(nums[mid]) != 0:
            if guess(nums[mid]) == -1:
                j = mid-1 
            elif guess(nums[mid]) == 1:
                i = mid+1
            mid=(j+i)//2

        return nums[mid]
        