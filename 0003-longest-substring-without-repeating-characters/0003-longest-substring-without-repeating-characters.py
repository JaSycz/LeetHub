from collections import defaultdict
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_len = 0
        for i in range(0,len(s)):
            if s[i] in substring:
                substring.clear()
                i = s.index(s[i])+1
                print(i)
            substring.add(s[i])
            max_len = max(max_len,len(substring))

        


                           
        
        return max_len
