# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node_a,node_b):
            if not node_a and not node_b:
                return True
            elif (node_a and not node_b) or (not node_a and node_b):
                return False

            if node_a.val != node_b.val:
                return False
            

            res_l = dfs(node_a.left,node_b.left)
            res_r = dfs(node_a.right,node_b.right)

            return (res_l and res_r) 

            
        
        
        return dfs(p,q)

        

