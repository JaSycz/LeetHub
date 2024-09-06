class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        
        que = list(senate)

        while que:
            if que[0] == 'R':
                if 'D' in que:
                    que.remove('D')
                else:
                    return "Radiant"
                que.append(que[0])
                que.pop(0)
            else:
                if 'R' in que:
                    que.remove('R')
                else:
                    return "Dire"
                que.append(que[0])
                que.pop(0)
        
        

        
        


            
            
                