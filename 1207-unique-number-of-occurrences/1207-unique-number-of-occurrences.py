class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_dict = {}

        for num in arr:
            freq_dict[num] = freq_dict.get(num,0)+1
            
        
        val = freq_dict.values()
        set_val = set(val)

        return len(val) == len(set_val)