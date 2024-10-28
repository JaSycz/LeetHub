class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited= set()
        stack = [0]
        
        while stack:
            
            room = stack.pop(-1)
            visited.add(room)
            for key in rooms[room]:
                if key in visited:
                    continue
                else:
                    stack.append(key)
                    
        
        print(visited)
        return len(visited) == len(rooms)


            

            