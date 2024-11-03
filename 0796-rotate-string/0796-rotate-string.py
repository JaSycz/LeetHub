class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
    

        for i in range(0,len(s)):
            i_str = []
            for n in range(i,len(s)+i):
                index = n % (len(s))
                i_str.append(s[index])
            if "".join(i_str) == goal:
                return True


        
        return False