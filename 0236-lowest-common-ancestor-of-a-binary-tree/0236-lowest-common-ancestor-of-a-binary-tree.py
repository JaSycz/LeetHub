# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
     

      
      def dfs(node,searched_node,path):
        if not node:
            return
        path.append(node)     
        if(node == searched_node):
            return path
            
        
        res = dfs(node.left,searched_node,path)
        if res:
            return res
        res = dfs(node.right,searched_node,path)
        if res:
            return res
        path.pop()  
        

      p_trace = dfs(root,p,[])
      q_trace = dfs(root,q,[])
      
      if len(p_trace) > len(q_trace):
        shorter_path = q_trace
      else:
        shorter_path = p_trace  
    
      for i in range(len(shorter_path)-1,-1,-1):
        print(i)
        if q_trace[i].val == p_trace[i].val:
           return q_trace[i]

      return shorter_path[-1]
        
