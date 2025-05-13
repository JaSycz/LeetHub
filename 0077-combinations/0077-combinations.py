class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        
        combinations = []
        comb = []
        def dfs(num):
            if len(comb) == k:
                combinations.append(comb[:]) 
                return

            for i in range(num,n+1):
                comb.append(i)
                dfs(i+1)
                comb.pop()

            
        dfs(1)
        
        return combinations
    
        

            
