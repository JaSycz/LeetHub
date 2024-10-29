class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        visited.add(0)
        adj = defaultdict(list)
        self.count = 0
        def dfs(city):
            for road in city:
                if road[0] in visited:
                    continue
                if road[1] == 0:
                    self.count+=1
                visited.add(road[0])
                dfs(adj[road[0]])    
                


        for i in range(n-1):
            adj[connections[i][0]].append([connections[i][1],0])
            adj[connections[i][1]].append([connections[i][0],-1])
        
        
        dfs(adj[0])


        return self.count
        