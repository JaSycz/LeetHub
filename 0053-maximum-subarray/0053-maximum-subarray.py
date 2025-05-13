class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_subarray = nums[0]

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum+= num
            max_subarray = max(max_subarray, curr_sum)

        return max_subarray