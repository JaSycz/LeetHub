from collections import defaultdict
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_pos = {}
        max_len = 0
        i=0

        while i<len(s):
            if s[i] in char_to_pos.keys():
                i = char_to_pos[s[i]]+1
                char_to_pos = {}  
                
            
            char_to_pos[s[i]] = i
            max_len = max(max_len,len(char_to_pos.keys()))
            i+=1
            print(i)

        


                           
        
        return max_len
