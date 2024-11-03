class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        start_indexes = []

        for i in range (0,len(s)):
            if s[i] == goal[0]:
                start_indexes.append(i)
        
        for start in start_indexes:
            shifted_s = []
            for i in range(start,len(s)+start):
                shifted_s.append(s[i%len(s)])
            if "".join(shifted_s) == goal:
                return True


        
        return False