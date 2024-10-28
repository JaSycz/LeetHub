class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited= [0]
        stack = [0]
        
        while stack:
            
            room = stack.pop(-1)
            
            for key in rooms[room]:
                if key in visited:
                    continue
                else:
                    stack.append(key)
                    visited.append(key)

                    
        
        print(visited)
        return len(visited) == len(rooms)


            

            