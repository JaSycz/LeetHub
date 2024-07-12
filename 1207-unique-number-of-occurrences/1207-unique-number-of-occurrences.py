class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_dict = {}

        for num in arr:
            if num  in freq_dict.keys():
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        val = freq_dict.values()
        set_val = set(val)

        return len(val) == len(set_val)