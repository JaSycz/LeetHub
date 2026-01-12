import math
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        queue = points.copy()
        pos = [queue[0][0],queue[0][1]]
        print(queue)
        queue.pop(0)
        
        time = 0
        move_options =[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        while queue:
            min_dist = float('inf')
            for mv in move_options:
                dist = max(abs(queue[0][0]-(pos[0]+mv[0])), abs(queue[0][1]-(pos[1]+mv[1])))
                
                if dist < min_dist:
                    min_dist = dist
                    move = mv

            pos[0]+=move[0]
            pos[1]+=move[1]
            
            if pos == queue[0]:
                queue.pop(0)
            
            time+=1
        
        return time
            