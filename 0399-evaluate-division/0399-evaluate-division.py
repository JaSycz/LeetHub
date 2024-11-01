import string
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        traces = defaultdict(list)

        def dfs(src,dst,vis,count):
            if src in vis:
                return
            vis.add(src)
            if src == dst:
                return count

            for val in traces[src]:
                ans = dfs(val[0],dst,vis,count*val[1])
                if ans:
                    return ans
            
                
        nodes = set()
        for i in range(len(equations)):
            traces[equations[i][0]].append([equations[i][1],values[i]])
            traces[equations[i][1]].append([equations[i][0],1.0/values[i]])
            nodes.add(equations[i][0])
            nodes.add(equations[i][1])
            
        
        results =[]
        for query in queries:
            if query[0] not in nodes or query[1] not in nodes:
                results.append(-1.0)
            else:
              vis = set()
              temp = 1.0
              ans = dfs(query[0],query[1],vis,temp)
              if ans:
                results.append(ans)
              else:
                results.append(-1.0)
        
        print(results)
        
        return results

