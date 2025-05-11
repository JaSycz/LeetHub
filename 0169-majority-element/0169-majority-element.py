from collections import defaultdict

class Solution:
    def map_frequencies(self, nums):
        freq = defaultdict(int)

        for i in nums:
            freq[i]+=1
        
        return freq
    
    def majorityElement(self, nums: List[int]) -> int:
        frequencies = self.map_frequencies(nums)
        

        return max(frequencies, key=frequencies.get)