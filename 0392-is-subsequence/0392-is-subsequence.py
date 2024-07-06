class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        i,j = 0,0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j+= 1
            i+= 1
        
        
        return j + 1 > len(s) and j != 0