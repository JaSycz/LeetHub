class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        

        x,y,cur =0,0,0

        for diff in differences:
            cur += diff
            x = min(x,cur)
            y = max(y,cur)
            if y - x > upper - lower:
                return 0

        return (upper-lower+1)-(y-x)
                
        
         