class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(src):
          for path in range(len(src)):
            if path not in visited and src[path] == 1:
                visited.add(path)
                dfs(isConnected[path])
                
        visited = set()
        provinces=0
        
        for node in range((len(isConnected))):
            if node not in visited:
              dfs(isConnected[node])
              provinces+=1
                
            


        return provinces

                
            
                

